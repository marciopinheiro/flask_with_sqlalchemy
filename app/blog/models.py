"""
Module that define blog models
"""
from datetime import datetime
from app.db import db

__all__ = (
    'Post',
)


class Post(db.orm.Model):
    """
    Post model class
    """
    __tablename__ = "posts"

    id = db.orm.Column(
        db.orm.Integer, 
        primary_key=True)

    author_id = db.orm.Column(
        db.orm.Integer, 
        db.orm.ForeignKey('users.id'), 
        nullable=False)

    author = db.orm.relationship(
        "User", 
        back_populates="posts")

    created = db.orm.Column(
        db.orm.DateTime, 
        nullable=False, 
        default=datetime.utcnow)

    title = db.orm.Column(
        db.orm.String, 
        unique=True, 
        nullable=False)

    body = db.orm.Column(
        db.orm.Text, 
        nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'
