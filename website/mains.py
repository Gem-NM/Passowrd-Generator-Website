from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db=SQLAlchemy()

DB_NAME = 'database.db'
def create_app():
    app=Flask(__name__)
    app.secret_key = 'super secret keyNitin'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from website.views import views
    from website.auth import auth

    from website.models import User
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    create_database(app)


    app.register_blueprint(views, url_prefix= '/')
    app.register_blueprint(auth, url_prefix= '/')
    
    

    return app

def create_database(app):
    if not path.exists('website/'+ DB_NAME):
        db.create_all(app=app)
        print("Database created")



