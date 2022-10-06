from flask_tutorial import login_manager, db
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    profile_picture = db.Column(db.String(70), nullable=False, default="default_img.jpg")
    password = db.Column(db.String(15), nullable=False)
    post = db.relationship("BlogPost", backref="auther", lazy=True)
    
    def __repr__(self):
        return f"User ({self.username})"