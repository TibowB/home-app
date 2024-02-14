from flask import render_template, redirect, url_for, request, abort
from models.User import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def index():
    return render_template("")

def store():
    pass
def show(userId):
    pass
def update(userId):
    pass
def delete(userId):
    pass
def destroy(userId): 
    pass
