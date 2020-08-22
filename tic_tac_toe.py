import re

from board import Board
from players.human_player import HumanPlayer
from players.random_computer import RandomComputerPlayer


class TicTacToe:

    def __init__(self):
        self._board = Board()

        p1 = HumanPlayer("X", self._board)
        # p2 = HumanPlayer("O", self._board)
        p2 = RandomComputerPlayer("0", self._board)

        self._players = [p1, p2]

    def start_game(self) -> None:
        turn = 0
        while not self._board.is_board_full() and self._board.winner() is None:
            player = turn % len(self._players)
            self._players[player].make_move()
            turn += 1
            print(self._board.gen_board_output())

        winner = self._board.winner()
        if winner:
            print(f"Winner is {winner}")
        else:
            print("Tie Game")





