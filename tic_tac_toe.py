import re

from board import Board


class TicTacToe:
    PLAYER_X = "X"
    PLAYER_O = "O"

    def __init__(self, players=2, markers=["X", "O"]):
        self.player_start = self.PLAYER_X
        self.board = Board()

    def start_game(self):


        move = input(f"Player {self.PLAYER_X}, please enter your move: ")
        processed_move = self.process_input(move)



        # print(self.board.gen_board_output)

    @staticmethod
    def process_input(input: str) -> str:
        # Regex expression accepting integers with optional whitespace before and after
        filtered_input = re.findall("^\s*\d+\s*,\s*\d+\s*$", input)
        if len(filtered_input) == 1:
            return filtered_input[0].replace(" ", "")   #strip all whitespace
        return None

