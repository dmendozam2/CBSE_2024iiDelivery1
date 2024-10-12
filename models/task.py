from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

     # Define the to_dict() method
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }