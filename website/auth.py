from flask import Blueprint,render_template,request,flash,redirect,url_for
from website.models import User
from website.mains import db
from flask_login import login_user,logout_user,current_user,login_required
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint('auth' , __name__)

@auth.route('login',methods = ['GET','POST'])

def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email  = email ).first()
        if user:
            if check_password_hash(user.password , password):
                login_user(user,remember=True)
                flash("logged In successfully")
                return redirect(url_for("views.home"))
    return render_template('login.html',user =current_user)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('auth.login'))

@auth.route('sign-up',methods = ['GET','POST'])
def signUp():
    if request.method =='POST':
        email = request.form.get('email')
        firstname= request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email  = email ).first()
        if user:
            flash('Email is already registered' ,category="error")
        elif len(email)<4:
            flash('Email must be grater than 3 characters' ,category="error")
            
        elif len(firstname)<2:
            flash('First name must be grater than 1 character' ,category="error")

        elif len(password1)<7:
            flash('Password must be grater than 6 characters' ,category="error")

        elif password1 != password2:
            flash('Passwords don\'t match' ,category="error")
        else:
            user = User(email=email,firstname=firstname , password = generate_password_hash(password1 ,method='sha256'))
            db.session.add(user)
            db.session.commit()
            login_user(user,remember=True)
            flash('Account Created' ,category="success")
            return redirect(url_for("views.home"))


        
    return render_template('signup.html',user=current_user)
