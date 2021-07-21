"""
Module that define blog views
"""
from flask import flash, g, redirect, render_template, request, url_for
from flask.views import MethodView
from sqlalchemy import desc

from app import db
from app.auth.decorators import login_required
from app.blog.utils import get_post
from app.blog.models import Post

__all__ = (
    'Index',
    'Create',
    'Update',
    'Delete'
)


class Index(MethodView):
    """
    Blog Index View class
    """
    def get(self):
        posts = Post.query.order_by(desc(Post.created)).all()
        return render_template('blog/index.html', posts=posts)


class Create(MethodView):
    """
    Blog Create View class
    """
    decorators = (login_required,)
    template = 'blog/create.html'

    def get(self):
        return render_template(self.template)

    def post(self):
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post = Post(
                title=title, 
                body=body, 
                author_id=g.user.id)

            db.orm.session.add(post)
            db.orm.session.commit()

            return redirect(url_for('blog.index'))

        return render_template(self.template)


class Update(MethodView):
    """
    Blog Update View class
    """
    decorators = (login_required,)
    template = 'blog/update.html'

    def get(self, id):
        post = get_post(id)
        return render_template(self.template, post=post)

    def post(self, id):
        post = get_post(id)

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

        return render_template(self.template)


class Delete(MethodView):
    """
    Blog Delete View class
    """
    decorators = (login_required,)

    def post(self, id):
        post = get_post(id)
        db.orm.session.delete(post)
        db.orm.session.commit()

        return redirect(url_for('blog.index'))
