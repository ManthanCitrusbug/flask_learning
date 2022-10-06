from datetime import datetime
from flask_tutorial import db    
    
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    discription = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(70), nullable=False, default="default.jpg")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    def __repr__(self):
        return f"BlogPost ({self.title})"