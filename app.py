from flask import Flask
from flask_migrate import Migrate

from models.Recipe import db

from controllers import home_bp, recipe_bp

app = Flask(__name__)

app.config.from_object("config")

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(home_bp)
app.register_blueprint(recipe_bp)


if __name__ == "__main__":
    app.run(debug=True)
