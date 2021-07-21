"""
Module that define app instance configuration
"""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
THREADS_PER_PAGE = 4
CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"


SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@postgres:5432/flask_with_sqlalchemy"
SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_CONNECT_OPTIONS = {}
