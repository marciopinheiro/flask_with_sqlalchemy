"""
Module that define app commands
"""
import click
from flask.cli import with_appcontext

from app.db import Database


@click.command('init-db')
@with_appcontext
def init_db_command():
    db = Database()
    db.orm.create_all()

    click.echo('Initialized the database.')
