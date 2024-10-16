import unittest
from app import app

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        """Test that the home page loads successfully"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_todo(self):
        """Test adding a new todo"""
        response = self.app.post('/todos', json={'todo': 'Test todo'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Todo added successfully', response.get_json()['message'])

    def test_list_todos(self):
        """Test listing todos"""
        # First, add a todo
        self.app.post('/todos', json={'todo': 'Test todo'})
        # Then, get the list of todos
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test todo', response.get_json())

    def test_delete_todo(self):
        """Test deleting a todo"""
        # First, add a todo
        self.app.post('/todos', json={'todo': 'Test todo'})
        # Then, delete the todo
        response = self.app.delete('/todos/0')
        self.assertEqual(response.status_code, 200)
        self.assertIn('deleted successfully', response.get_json()['message'])

if __name__ == '__main__':
    unittest.main()
