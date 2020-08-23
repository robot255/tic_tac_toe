import random

from board import Board
from players.player import Player


class RandomComputerPlayer(Player):
    def __init__(self, marker: str, board: Board):
        super(RandomComputerPlayer, self).__init__(marker)
        self._board = board

    def make_move(self) -> None:
        size = self._board.get_size
        valid_spot = False
        while not valid_spot:
            x = random.randint(0, size)
            y = random.randint(0, size)
            valid_spot, _ = self._board.is_valid_location(x, y)

        print(f"AI has selected {x},{y}")
        self._board.update(x, y)
