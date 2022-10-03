from urllib import request
from flask import flash, render_template, redirect, url_for
from flask_tutorial import db, app, bcrypt
from flask_tutorial.forms import LoginForm, RegistraionForm, AddPost
from flask_tutorial.models import BlogPost, User
from flask_login import login_user, current_user, login_required, logout_user
# db.drop_all()
db.create_all()

@app.route("/register", methods=['GET', 'POST'])
def register(): 
    form = RegistraionForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Registered successfully {form.username.data}", "success")
        return redirect(url_for("login"))
    return render_template('register.html', form=form)


@app.route("/", methods=['GET', 'POST'])
# @login_required
def home():
    if not current_user.is_authenticated:
        return redirect(url_for("register"))
    else :
    # qry_user = User.query.all()
        qry_post = BlogPost.query.filter_by(user_id=current_user.id)
        return render_template('home.html', posts=qry_post)
    # return render_template('home.html', users=qry_user)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("home"))
        flash("Login successfully", "success")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/add_post", methods=['GET', 'POST'])
def add_post():
    form = AddPost()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, discription=form.discription.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_post.html", form=form)


@app.route("/<int:post_id>/delete", methods=['GET', 'POST'])
def delete_post(post_id):
    post = BlogPost.query.filter_by(id=int(post_id)).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    # post = BlogPost.query.get_or_404(post_id)
    post = BlogPost.query.filter_by(id=int(post_id)).first()
    form = AddPost()
    if form.validate_on_submit():
        post.title = form.title.data
        post.discription = form.discription.data
        post.user_id = current_user.id
        db.session.commit()
        return redirect(url_for("home"))
    else:
        form.title.data = post.title
        form.discription.data = post.discription
        current_user.id = post.user_id
        return render_template("update_post.html", form=form, post=post)