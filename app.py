import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask, request, jsonify, send_from_directory

sentry_sdk.init(
    dsn="https://39b3591d4c0e71768cc5dcd58e0afcec@o4508130204778496.ingest.us.sentry.io/4508130206416896",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = Flask(__name__)

# In-memory storage for todos
todos = []
completed_todos = 0

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
        completed_todos += 1
        return jsonify({"message": f"Todo '{deleted_todo}' deleted successfully"}), 200
    return jsonify({"error": "Todo not found"}), 404

if __name__ == '__main__':
    # lets see what percent of our todos are complete
    print(completed_todos / len(todos) * 100)
    app.run(host='0.0.0.0', port=8080)