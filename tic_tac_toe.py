import re

from board import Board, State
from players.human_player import HumanPlayer
from players.random_computer import RandomComputerPlayer
from players.minimax_computer import MinMaxComputerPlayer


class TicTacToe:

    def __init__(self):
        self._board = Board(size=4)

        p1 = HumanPlayer("X", self._board)
        p2 = MinMaxComputerPlayer("O", self._board)

        self._players = [p1, p2]

    def start_game(self) -> None:
        turn = 0
        while self._board.get_state == State.INPLAY:
            player = turn % len(self._players)
            self._players[player].make_move()
            turn += 1
            print(self._board.gen_board_output())

        if self._board.get_state == State.DRAW:
            print("Tie Game")
        else:
            print(f"Winner is {self._board.get_winner}")





