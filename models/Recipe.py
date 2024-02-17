from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # duration = db.Column(db.Integer)
    # difficulty = db.Column(db.Integer)

    def __init__(self, name: str) -> None:
        self.name = name
        # self.duration = duration
        # self.duration = difficulty

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # 'duration': self.duration,
            # 'difficulty': self.difficulty
        }
