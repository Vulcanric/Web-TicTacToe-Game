import unittest
from app.models import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_make_move(self):
        """Test making a move on the Tic Tac Toe board."""
        game = TicTacToe()
        game.make_move(0, 'X')
        self.assertEqual(game.board[0], 'X')
    
    def test_ai_move(self):
        """Test the AI making a move."""
        game = TicTacToe()
        game.make_move(0, 'X')
        move = game.ai_move()
        self.assertIsInstance(move, int)
    
    def test_check_winner(self):
        """Test the check winner function."""
        game = TicTacToe()
        game.make_move(0, 'X')
        game.make_move(1, 'X')
        game.make_move(2, 'X')
        self.assertEqual(game.current_winner, 'X')

if __name__ == "__main__":
    unittest.main()
