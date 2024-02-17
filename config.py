import os

SECRET_KEY = os.urandom(32)

# Connect to the database
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres123$@localhost/home_app_db"

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
