import unittest
from tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.tic_tac_toe = TicTacToe()

    def test_player_x_starts(self):
        self.assertTrue(self.tic_tac_toe.player_start == "X")


if __name__ == '__main__':
    unittest.main()
