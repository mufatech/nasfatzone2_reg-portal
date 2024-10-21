from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_login import LoginManager



app = Flask(__name__);
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'


# load environment variables .env file
load_dotenv()

# load secret key from enviroment variable
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


# load database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)

with app.app_context():
    from . import routes # Import routes
    
    db.create_all()  # create tables
    
#return app

from app.routes.root import *
from app.routes.admin import *
from app.models.user import *
from app.models.admin import *
