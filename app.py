from flask import Flask, render_template, redirect, url_for, request
from flask_migrate import Migrate
from sqlalchemy import select

from models.Recipe import db, Recipe

app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)

migrate = Migrate(app, db)


@app.route("/")
def index():
    recipes = db.session.execute(select(Recipe)).scalars().all()
    return render_template("index.html", recipes=recipes)


@app.route("/recipes/create", methods=["GET", "POST"])
def create_recipe():
    if request.method == "POST":
        recipe = Recipe(name=request.form["name"])
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("recipe.html")


@app.route("/recipes/delete/<id>", methods=["POST"])
def delete_recipe(id):
    recipe = db.get_or_404(Recipe, id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
