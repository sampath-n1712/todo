import os
import username, password, key from ../secrets.py

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/todo_app_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key
SECRET_KEY = key