import unittest
import os
import sys

# Add the parent directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # assuming your Flask app is in a file named app.py

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        response = self.app.post('/add', data=dict(todoitem='Test task'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_clear(self):
        response = self.app.post('/clear', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_complete(self):
        response = self.app.get('/complete/1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()