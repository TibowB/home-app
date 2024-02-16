from flask import Flask, render_template
from flask_migrate import Migrate
from sqlalchemy import select

from models.Recipe import db, Recipe
from routes.user_bp import user_bp

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/users')

@app.route('/')
def index():
    recipes = db.session.execute(select(Recipe)).scalars().all()
    return render_template('index.html', recipes=recipes)

if __name__ == '__main__':
    app.debug = True
    app.run()