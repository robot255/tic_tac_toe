import re

from board import Board, State
from players.human_player import HumanPlayer
from players.random_computer import RandomComputerPlayer
from players.minimax_computer import MinMaxComputerPlayer


class TicTacToe:

    def __init__(self):
        self._board = Board()

        p1 = HumanPlayer("X", self._board)
        # p2 = HumanPlayer("O", self._board)
        # p2 = RandomComputerPlayer("0", self._board)
        p2 = MinMaxComputerPlayer("O", self._board)

        self._players = [p1, p2]

    def start_game(self) -> None:
        turn = 0
        while self._board.get_state == State.INPLAY:
            player = turn % len(self._players)
            self._players[player].make_move()
            turn += 1
            print(self._board.gen_board_output())

        if State.WINNER:
            print(f"Winner is {self._board.get_winner}")
        else:
            print("Tie Game")





