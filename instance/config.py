"""
Module that define app instance configuration
"""
import os

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(BASE_DIR, "app.db")
SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 4

CSRF_ENABLED = True

CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"
