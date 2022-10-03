import imp
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, ValidationError
from flask_tutorial.models import User
from flask_tutorial import bcrypt


class RegistraionForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired(), validators.Length(min=2, max=15)])
    email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=2, max=10)])
    confirm_password = PasswordField("Confirm Password", validators=[validators.DataRequired(), validators.EqualTo("password")])
    submit = SubmitField("Sing Up")
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username is already exist. Please try another.")
        
    def validate_email(self, email):
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError("This email is already exist. Please try another.")
    
    
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=2, max=10)])
    submit = SubmitField("Sing In")
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("Check your email id or password.")
        
        
class AddPost(FlaskForm):
    title = StringField("Title", validators=[validators.Length(min=2, max=70)])
    discription = StringField("Discription", validators=[validators.DataRequired()])
    submit = SubmitField("Add Post")