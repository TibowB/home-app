from flask import Blueprint, render_template
from sqlalchemy import select
from models import Recipe, db


home_bp = Blueprint("home_bp", __name__)


def index():
    recipes = db.session.execute(select(Recipe)).scalars().all()
    return render_template("index.html", recipes=recipes)


home_bp.route("/", methods=["GET"])(index)
