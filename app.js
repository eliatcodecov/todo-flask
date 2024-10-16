document.addEventListener('DOMContentLoaded', () => {
    const todoForm = document.getElementById('todo-form');
    const todoInput = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');

    function fetchTodos() {
        fetch('/todos')
            .then(response => response.json())
            .then(todos => {
                todoList.innerHTML = '';
                todos.forEach((todo, index) => {
                    const li = document.createElement('li');
                    li.textContent = todo;
                    const deleteBtn = document.createElement('button');
                    deleteBtn.textContent = 'Delete';
                    deleteBtn.classList.add('delete-btn');
                    deleteBtn.onclick = () => deleteTodo(index);
                    li.appendChild(deleteBtn);
                    todoList.appendChild(li);
                });
            });
    }

    function addTodo(todo) {
        fetch('/todos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ todo: todo }),
        })
        .then(response => response.json())
        .then(() => {
            fetchTodos();
            todoInput.value = '';
        });
    }

    function deleteTodo(index) {
        fetch(`/todos/${index}`, { method: 'DELETE' })
            .then(response => response.json())
            .then(() => fetchTodos());
    }

    todoForm.onsubmit = (e) => {
        e.preventDefault();
        addTodo(todoInput.value);
    };

    fetchTodos();
});
