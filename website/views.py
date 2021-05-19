from flask import Blueprint,render_template,request,flash
from flask_login import current_user,login_required
from website.calc.randomnum import password_gen
from website.calc.cus_pass import cuss_pass_gen

views = Blueprint('views' , __name__)

@views.route("/")
@login_required
def home():
    return render_template('home.html',user=current_user)

@views.route("Ran_Pass_gen", methods=['GET' ,'POST'])
def random():
    if request.method == 'POST':
        password = password_gen()
        return render_template('num.html',nums=password,user=current_user)
    else:
        return render_template('ran.html',user=current_user)

@views.route("Cus_Pass_gen" ,methods=['GET' ,'POST'])
def custom():
    if request.method == 'POST':
        alpha = int(request.form.get('abc'))
        numbers = int(request.form.get('nums'))
        schar = int(request.form.get('schar'))
        if alpha<=0:
            flash("No. of alphabets cannot be less than or equal to 0",category="error")
            return render_template('cus.html')
        elif numbers<=0:
            flash("No. of numricals cannot be less than or equal to 0",category="error")
            return render_template('cus.html')
        elif schar<=0:
            flash("No. of special cahracters cannot be less than or equal to 0",category="error")
            return render_template('cus.html')
        elif alpha+schar+numbers <7:
            flash("Length of password should not be less than 7",category="error")
            return render_template('cus.html',user=current_user)

        else:
            flash('Password Generated Succesfuly', category="success")
            cuss_pass= cuss_pass_gen(alpha,numbers,schar)
            return render_template('cus_num.html',cus_num=cuss_pass,abc=alpha,nums=numbers,schar=schar,user=current_user)
    else:
        return render_template('cus.html',user=current_user)
