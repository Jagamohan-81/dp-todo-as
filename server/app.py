from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}) 

todos = []
todo_id_counter = 1  

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def create_todo():
    global todo_id_counter
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400

    new_todo = {
        "id": todo_id_counter,
        "title": data["title"],
        "completed": False
    }
    todos.append(new_todo)
    todo_id_counter += 1
    return jsonify(new_todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200

@app.route('/api/todos/<int:todo_id>', methods=['PATCH'])
def toggle_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = not todo["completed"]
            return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)
