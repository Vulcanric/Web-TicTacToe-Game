import unittest
from app import create_app, db
from flask import json

class TicTacToeTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test variables and initialize the app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        
        with self.app.app_context():
            db.create_all()
    
    def tearDown(self):
        """Tear down the test variables."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_index(self):
        """Test the index route."""
        response = self.client().get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tic Tac Toe', response.data)
    
    def test_play_ai(self):
        """Test the play-ai route."""
        response = self.client().post('/play-ai', json={'move': 0})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('ai_move', data)
        self.assertIn('winner', data)

if __name__ == "__main__":
    unittest.main()
