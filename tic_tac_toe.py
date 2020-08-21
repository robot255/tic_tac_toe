class TicTacToe:

    PLAYER_X = "X"
    PLAYER_O = "O"

    def __init__(self):
        self.player_start = self.PLAYER_X

    def start_game(self):
        input(f"Player {self.PLAYER_X}, please enter your move: ")
