"""
Module that define auth views
"""
from flask import flash, g, redirect, render_template, request, session, url_for
from flask.views import MethodView
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.auth.models import User

__all__ = (
    'load_logged_in_user',
    'Register', 
    'Login', 
    'Logout'
)


def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


class Register(MethodView):
    """
    Auth Register View class
    """
    template = 'auth/register.html'

    def get(self):
        return render_template(self.template)

    def post(self):
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not User.query.filter_by(username=username):
            error = 'User {} is already registered.'.format(username)

        if error is None:
            user = User(
                username=username,
                password=generate_password_hash(password))

            db.orm.session.add(user)
            db.orm.session.commit()

            return redirect(url_for('auth.login'))

        flash(error)
        return render_template(self.template)


class Login(MethodView):
    """
    Auth Login View class
    """
    template = 'auth/login.html'

    def get(self):
        return render_template(self.template)

    def post(self):
        username = request.form['username']
        password = request.form['password']
        error = None

        user = User.query.filter_by(username=username).first_or_404()
        
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))

        flash(error)
        return render_template(self.template)


class Logout(MethodView):
    """
    Auth Logout View class
    """
    def get(self):
        session.clear()
        return redirect(url_for('index'))
