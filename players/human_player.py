import re

from players.player import Player
from board import Board
from typing import Tuple


class HumanPlayer(Player):
    def __init__(self, marker: str, board: Board = None):
        super(HumanPlayer, self).__init__(marker)
        self._board = board

    def make_move(self) -> None:
        valid_move = False

        while not valid_move:
            move = self.get_input(f"Player {self._marker}, please enter your move x,y: \n")
            processed_move = self.process_input(move)
            if processed_move:
                valid_move, msg = self._board.is_valid_location(processed_move[1], processed_move[0])

                if valid_move:
                    continue
            else:
                print(f"""Unable to process your move '{move}'.
                          Valid moves must be entered in the format x,y 
                          Valid moves are between 0 and 999""")
                continue
            if not valid_move:
                print(f"Move {move} is invalid because {msg}")

        x, y = processed_move
        print(f'Human Player move is {x},{y}')
        self._board.update(y, x)

    @staticmethod
    def get_input(text):
        return input(text)

    @staticmethod
    def process_input(user_input: str) -> Tuple[int, int]:
        # Regex expression accepting integers with optional whitespace before and after
        filtered_input = re.findall(r"^\s*\d{1,3}\s*,\s*\d{1,3}\s*$", user_input)
        if len(filtered_input) == 1:
            x, y = filtered_input[0].replace(" ", "").split(",")
            return int(x), int(y)  # since the number of digits is limited to 3 no risk of overflow
        return None
