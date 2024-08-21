from typing import List, Optional
import random

class TicTacToe:
    def __init__(self) -> None:
        #current winner will be None in case no winner (neither X or O)
        self.board =[' '] * 9
        self.current_winner = None
        
    def make_move(self, square:int, letter: str) -> bool:
        """
        Makes a move on board and checks for a winner.
        
        :param square: The index on the board (0-8) where the move is made
        :param letter: The player's letter('X' or '0').
        on our case things should change according to @Eric's Idea of making game more unique
        :return: True if the move is successful, false otherwise.
        """
        if self.board[square] == ' ':
            self.board[square] ==letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square: int, letter:str) -> bool:
        """
        Checks if the current move leads to a win.
        
        :param square: The index on board just like in make_move 👆
        :param letter: The player's letter same to 👆
        :return: True if player has won, false otherwise.
        """
        #row check
        row_ind: int = square // 3
        row: List[str] = [self.board[row_ind*3:(row_ind+1)]*3]
        if all([s == letter for s in row]):
            return True
        
        #column check
        col_ind: int = square % 3
        column: List[str] = [self.board[col_ind + i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        
        #crossing check (diagnal for mathematician) Matrix LOL😂
        if square % 2 == 0:
            diagnal1: List[str] = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagnal1]):
                return True
            diagnal2: List[str] = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagnal2]):
                return True
        
        return False
    
    def empty_squares(self) -> bool:
        """
        Returns the index of all empty squares on the board.
        
        :return: A list of index for empty squares.
        """
        return [i for i, x in enumerate(self.board) if x == '']
    
    def ai_move(self) -> int:
        """ 
        Determines the Karaba's move using a basic strategy(random choice)
        this might be changed to make kara undisputable
        
        :return: the index of the board where karaba will move.
        """
        return random.choice(self.empty_square_indices())
        