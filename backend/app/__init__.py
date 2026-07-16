from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ba75c255983c24387fc22ce96a71a507'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

loginmngr = LoginManager(app)
loginmngr.login_view = 'login'


CORS(app, origins = ["http://localhost:5173"])

from app import routes

from app.api.auth import auth

app.register_blueprint(auth, url_prefix="/api")