"""
Module that define blog views
"""
from flask import flash, g, redirect, render_template, request, url_for
from sqlalchemy import desc

from app import db
from app.auth.decorators import login_required
from app.blog import blog
from .services import get_post
from app.blog.models import Post


@blog.route('/')
def index():
    posts = Post.query.order_by(desc(Post.created)).all()
    return render_template('blog/index.html', posts=posts)


@blog.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post = Post(title=title, body=body, author_id=g.user.id)
            db.orm.session.add(post)
            db.orm.session.commit()

            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


@blog.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post.title = title
            post.body = body
            db.orm.session.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@blog.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    post = get_post(id)
    db.orm.session.delete(post)
    db.orm.session.commit()
    return redirect(url_for('blog.index'))

