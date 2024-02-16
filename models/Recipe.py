from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipe(db.Model):
    __tablename__ = 'recipes' 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }