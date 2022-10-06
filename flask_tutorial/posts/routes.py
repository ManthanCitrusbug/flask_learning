import secrets, os
from flask import render_template, redirect, url_for, Blueprint, request
from flask_login import current_user
from flask_tutorial import db, app
from flask_tutorial.posts.forms import AddPost
from flask_tutorial.posts.models import BlogPost

posts = Blueprint("posts", __name__)

@posts.route("/add_post", methods=['GET', 'POST'])
def add_post():
    form = AddPost()
    if form.validate_on_submit():
        if form.image.data:
            hex_image = secrets.token_hex(8)
            f_name, f_ext = os.path.splitext(form.image.data.filename)
            image_name = hex_image + f_ext
            image_path = os.path.join(app.root_path, 'static\images', image_name)
            form.image.data.save(image_path)
        post = BlogPost(title=form.title.data, discription=form.discription.data, image=image_name, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("user.home"))
    return render_template("add_post.html", form=form)


@posts.route("/<int:post_id>/delete", methods=['GET', 'POST'])
def delete_post(post_id):
    post = BlogPost.query.filter_by(id=int(post_id)).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('user.home'))


@posts.route("/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    # post = BlogPost.query.get_or_404(post_id)
    post = BlogPost.query.filter_by(id=int(post_id)).first()
    form = AddPost()
    if form.validate_on_submit():
        if form.image.data:
            hex_image = secrets.token_hex(8)
            f_name, f_ext = os.path.splitext(form.image.data.filename)
            image_name = hex_image + f_ext
            image_path = os.path.join(app.root_path, 'static\images', image_name)
            form.image.data.save(image_path)
        post.title = form.title.data
        post.discription = form.discription.data
        post.image = image_name
        post.user_id = current_user.id
        db.session.commit()
        return redirect(url_for("user.home"))
    else:
        form.title.data = post.title
        form.discription.data = post.discription
        form.image.data = post.image
        return render_template("update_post.html", form=form, post=post)
    

@posts.route("/<int:post_id>/detail", methods=['GET', 'POST'])
def detail(post_id):
    post = BlogPost.query.filter_by(id=post_id).first()
    return render_template("detail_post.html", post=post)