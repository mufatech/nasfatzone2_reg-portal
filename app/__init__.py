from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv  # Import the load_dotenv function
from flask_login import LoginManager
from flask_login import current_user
from flask_mail import Mail
from flask_migrate import Migrate


# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

# Load secret key from environment variable
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

# Load database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'
migrate = Migrate(app, db)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get("MAIL_USERNAME")


mail = Mail(app)



@login_manager.user_loader
def load_user(user_id):
    # You don't need to check current_user.is_authenticated here
    # Simply return the user with the given ID
    from app.models.admin import Admin  # Import here to avoid circular import
    return Admin.query.get(int(user_id))


from app.routes.root import *
from app.routes.admin import *
from app.routes.user import *

if __name__ == '__main__':
    app.run()
