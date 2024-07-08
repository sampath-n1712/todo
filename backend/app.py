# backend/app.py
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('config.py')
CORS(app)
db = SQLAlchemy(app)

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

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.serialize() for todo in todos])

@app.route('/api/todos', methods=['POST'])
def create_todo():
    content = request.json.get('content', '')
    if content:
        new_todo = Todo(content=content)
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({'message': 'Todo created successfully'}), 201
    return jsonify({'error': 'Content is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
