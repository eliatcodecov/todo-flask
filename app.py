from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# In-memory storage for todos
todos = []

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/app.js')
def serve_js():
    return send_from_directory('.', 'app.js')

@app.route('/todos', methods=['GET', 'POST'])
def manage_todos():
    if request.method == 'GET':
        return jsonify(todos)
    elif request.method == 'POST':
        todo = request.json.get('todo')
        if todo:
            todos.append(todo)
            return jsonify({"message": "Todo added successfully"}), 201
        return jsonify({"error": "Invalid todo"}), 400

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        deleted_todo = todos.pop(todo_id)
        return jsonify({"message": f"Todo '{deleted_todo}' deleted successfully"}), 200
    return jsonify({"error": "Todo not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
