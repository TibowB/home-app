from flask import Blueprint, render_template, request, redirect, url_for
from models import Recipe, db


recipe_bp = Blueprint("recipe_bp", __name__, url_prefix="/recipes")


def create_recipe():
    if request.method == "POST":
        recipe = Recipe(name=request.form["name"])
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("home_bp.index"))

    return render_template("recipe.html")


def delete_recipe(id):
    recipe = db.get_or_404(Recipe, id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("home_bp.index"))


recipe_bp.route("/create", methods=["GET", "POST"])(create_recipe)
recipe_bp.route("/delete/<id>", methods=["GET", "POST"])(delete_recipe)
