# backend/models.py
from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'completed': self.completed
        }
