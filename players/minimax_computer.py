import random
import math
import copy

from players.player import Player
from board import Board, State


class MinMaxComputerPlayer(Player):
    def __init__(self, marker: str, board: Board):
        super(MinMaxComputerPlayer, self).__init__(marker)
        self._board = board
        self.player_markers = ["X", "O"]

    def make_move(self) -> None:
        bestScore = -math.inf
        best_x = None
        best_y = None

        for x, y in self._board.get_possible_moves():
            self._board.update(x, y)
            score = self.minimax(False, self._marker, self._board)
            self._board.undo()
            if score > bestScore:
                bestScore = score
                best_x = x
                best_y = y
        print("Minmax  algorithms select {best_x},{best_y}")
        self._board.update(best_x, best_y)

    def minimax(self, is_max, maximizer_marker, curr_board) -> int:
        state = curr_board.get_state
        if state is State.DRAW:
            return 0
        elif state is State.WINNER:
            return 1 if curr_board.get_winner is maximizer_marker else -1

        scores = []
        for x, y in curr_board.get_possible_moves():
            curr_board.update(x, y)
            scores.append(self.minimax(not is_max, maximizer_marker, curr_board))
            curr_board.undo()
            if (is_max and max(scores) == 1) or (not is_max and min(scores) == -1):
                break

        return max(scores) if is_max else min(scores)
