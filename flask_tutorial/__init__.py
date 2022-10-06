from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e670ea4ac75d3720402ec47951f08494'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_practice.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flask_tutorial.user.routes import user
from flask_tutorial.posts.routes import posts

app.register_blueprint(user)
app.register_blueprint(posts)