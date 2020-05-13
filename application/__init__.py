from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('FLASK_BLOG_DB_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes
