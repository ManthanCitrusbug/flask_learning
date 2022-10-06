from flask import Blueprint
from flask import flash, render_template, redirect, url_for, request
from flask_login import login_user, current_user, login_required, logout_user
from flask_tutorial import db, bcrypt
from flask_tutorial.user.forms import RegistraionForm, LoginForm
from flask_tutorial.posts.models import BlogPost
from flask_tutorial.user.models import User

user = Blueprint("user", __name__)


@user.route("/register", methods=['GET', 'POST'])
def register(): 
    form = RegistraionForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Registered successfully {form.username.data}", "success")
        return redirect(url_for("user.login"))
    return render_template('register.html', form=form)


@user.route("/")
@login_required
def home():
    page  = request.args.get('page', 1, type=int)
    if not current_user.is_authenticated:
        return redirect(url_for("register"))
    else :
        qry_post = BlogPost.query.filter_by(user_id=current_user.id).paginate(per_page=2, page=page)
        return render_template('home.html', posts=qry_post)


@user.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("user.home"))
        flash("Login successfully", "success")
    return render_template("login.html", form=form)


@user.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("user.login"))