from typing import List, Optional
import random
import time

class TicTacToe:
    def __init__(self) -> None:
        """
        Initializes the TicTacToe board and sets the current winner to None.
        """
        self.board = [' '] * 9
        self.current_winner: Optional[str] = None

    def make_move(self, square: int, letter: str) -> bool:
        """
        Makes a move on the board and checks for a winner.
        
        :param square: The index on the board (0-8) where the move is made.
        :param letter: The player's letter ('X' or 'O').
        :return: True if the move is successful, false otherwise.
        """
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square: int, letter: str) -> bool:
        """
        Checks if the current move leads to a win.
        
        :param square: The index on the board where the move is made.
        :param letter: The player's letter ('X' or 'O').
        :return: True if the player has won, false otherwise.
        """
        # Row check
        row_ind = square // 3
        row: List[str] = self.board[row_ind*3:(row_ind+1)*3]
        if all(s == letter for s in row):
            return True
        
        # Column check
        col_ind = square % 3
        column: List[str] = [self.board[col_ind + i*3] for i in range(3)]
        if all(s == letter for s in column):
            return True
        
        # Diagonal check
        if square % 2 == 0:
            # Check both diagonals if the move is on an even square
            diagonal1: List[str] = [self.board[i] for i in [0, 4, 8]]
            diagonal2: List[str] = [self.board[i] for i in [2, 4, 6]]
            if all(s == letter for s in diagonal1) or all(s == letter for s in diagonal2):
                return True
        
        return False
    
    def empty_squares(self) -> List[int]:
        """
        Returns a list of all empty squares on the board.
        
        :return: A list of indices for empty squares.
        """
        return [i for i, x in enumerate(self.board) if x == ' ']

    def num_empty_squares(self) -> int:
        """
        Returns the number of empty squares on the board.
        
        :return: The count of empty squares.
        """
        return self.board.count(' ')

    def ai_move(self) -> int:
        """ 
        Determines the AI's move using a basic strategy (random choice).
        
        :return: The index on the board where the AI will move.
        """
        time.sleep(3)  # Delay to simulate thinking time
        return random.choice(self.empty_squares())
    
    def is_full(self) -> bool:
        """
        Checks if the board is full.
        
        :return: True if the board is full, False otherwise.
        """
        return ' ' not in self.board

    def reset_board(self) -> None:
        """
        Resets the board for a new game, clearing all moves.
        """
        self.board = [' '] * 9
        self.current_winner = None

    def game_over(self) -> bool:
        """
        Checks if the game is over, either by a win or a draw.
        
        :return: True if the game is over, False otherwise.
        """
        return self.current_winner is not None or self.is_full()
