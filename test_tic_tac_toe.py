import unittest
from parameterized import parameterized
from tic_tac_toe import TicTacToe
from board import Board
from typing import List


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.tic_tac_toe = TicTacToe()

    # Game Unit Tests
    def test_player_x_starts(self):
        self.assertTrue(self.tic_tac_toe.player_start == "X")

    # Board Test
    @parameterized.expand([["0,0 X", 3, 0, 0, "X", '  0 1 2\n0 X| | \n  -----\n1  | | \n  -----\n2  | | \n'],
                           ["1,1 O", 3, 1, 1, "O", '  0 1 2\n0  | | \n  -----\n1  |O| \n  -----\n2  | | \n'],
                           ["2,2 P", 3, 2, 2, "P", '  0 1 2\n0  | | \n  -----\n1  | | \n  -----\n2  | |P\n'],
                           ["3,3 W", 4, 3, 3, "W",
                            '  0 1 2 3\n0  | | | \n  ------\n1  | | | \n  ------\n2  | | | \n  ------\n3  | | |W\n']])
    def test_gen_board_output_and_updates(self, name: str, s: int, x: int, y: int, marker: str, result: str):
        board = Board(size=s)
        board.update(x, y, marker)
        self.assertEqual(board.gen_board_output(), result)

    @parameterized.expand([["valid_move 0 0", 3, 0, 0, True],
                           ["valid_move 1 1", 3, 1, 1, True],
                           ["invalid_move -1 0", 3, -1, 0, False],
                           ["invalid_move 0 -1", 3, 0, -1, False],
                           ["invalid_move 0 3", 3, 0, 3, False],
                           ["invalid_move", 3, 3, 0, False],
                           ["invalid_move", 4, 4, 3, False],
                           ["invalid_move", 4, 3, 4, False],
                           ["valid_move", 4, 3, 3, True]])
    def test_board_is_valid_move(self, name: str, s: int, x: int, y: int,  result: str):
        board = Board(size=s)
        self.assertEqual(board.is_valid_location(x, y), result)

    # In a 3x3 tic tac toe board there is 8 possible way of winning
    @parameterized.expand([["no win blank board", 3, 3, [[None, None, None],
                                                         [None, None, None],
                                                         [None, None, None]], None],
                           ["X wins horizontal first row", 3, 3, [["X", "X", "X"],
                                                                  ["O", "O", None],
                                                                 [None, None, None]], "X"],
                           ["O wins horizontal second row", 3, 3, [["X", "O", "O"],
                                                                  ["O", "O", "O"],
                                                                  ["X", None, "X"]], "O"],
                           ["X wins horizontal third row", 3, 3, [["X", "O", "O"],
                                                                  ["O", "O", "X"],
                                                                  ["X", "X", "X"]], "X"],
                           ["O wins vertical first column", 3, 3, [["O", "X", "X"],
                                                                   ["O", "O", "X"],
                                                                   ["O", "X", "O"]], "O"],
                           ["O wins vertical second column", 3, 3, [["X", "O", "O"],
                                                                    ["O", "O", "X"],
                                                                    ["X", "O", "X"]], "O"],
                           ["X wins vertical third column", 3, 3, [["X", "O", "X"],
                                                                   ["O", None, "X"],
                                                                   ["X", "O", "X"]], "X"],
                           ["X wins diagonal third column", 3, 3, [["O", "O", "X"],
                                                                   ["O", "X", "O"],
                                                                   ["X", "O", "X"]], "X"],
                           ["X wins diagonal third column", 3, 3, [["X", "O", "O"],
                                                                   ["O", "X", "O"],
                                                                   ["X", "O", "X"]], "X"],
                           ])
    def test_board_winner(self, name: str, s: int, wc: int, board_setup: List[List],  result: str):
        board = Board(size=s, win_count=wc)
        board._board = board_setup
        self.assertEqual(board.winner(), result)



if __name__ == '__main__':
    unittest.main()
