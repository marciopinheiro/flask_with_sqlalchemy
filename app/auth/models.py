"""
Module that define auth models
"""
from app.db import db

__all__ = (
    'User',
)


class User(db.orm.Model):
    """
    Auth model class
    """
    __tablename__ = "users"

    id = db.orm.Column(
        db.orm.Integer, 
        primary_key=True)

    username = db.orm.Column(
        db.orm.String, 
        unique=True, 
        nullable=False)

    password = db.orm.Column(
        db.orm.String, 
        nullable=False)

    posts = db.orm.relationship(
        "Post", 
        back_populates="author", 
        lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
