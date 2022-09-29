from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class RegistraionForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired(), validators.Length(min=2, max=15)])
    email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=2, max=10)])
    confirm_password = PasswordField("Confirm Password", validators=[validators.DataRequired(), validators.EqualTo("password")])
    submit = SubmitField("Sing Up")
    
    
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=2, max=10)])
    submit = SubmitField("Sing In")