from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
import os

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
login_manager = LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = basedir+'/static/media/'