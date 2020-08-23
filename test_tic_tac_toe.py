import unittest

from unittest.mock import MagicMock, Mock
from parameterized import parameterized
from tic_tac_toe import TicTacToe
from board import Board, State
from players.human_player import HumanPlayer
from players.random_computer import RandomComputerPlayer
from players.minimax_computer import MinMaxComputerPlayer
from typing import List, Tuple


class TestTicTacToe(unittest.TestCase):

    # Basic Integration tests to test that everything is working as expected run throw a full game
    @parameterized.expand([["Draw 1", ["0,1", "1,1", "2,0", "1,2", "2,2"], State.DRAW, None],
                           ["Computer Wins 1", ["1,1", "1,0", "2,0", "2,2"], State.WINNER, "O"]])
    def test_integrations(self, name: str, moves: List[Tuple[int, int]], state: State, winner: str):
        tic_tac_toe = TicTacToe()

        mock_player = HumanPlayer("X", tic_tac_toe._board)
        mock_player.get_input = Mock()
        mock_player.get_input.side_effect = moves
        tic_tac_toe._players[0] = mock_player
        tic_tac_toe.start_game()

        self.assertEquals(tic_tac_toe._board.get_state, state)
        self.assertEquals(tic_tac_toe._board.get_winner, winner)

    #############################
    #  Human Player Unit Test   #
    #############################
    @parameterized.expand([["Invalid user_input strings", "not correct user_input", None],
                           ["Invalid user_input strings with ,", "not,user_input", None],
                           ["Invalid user_input strings with digits ,", "0.0,1.1", None],
                           ["Invalid user_input strings with digits , A", "A,1.1", None],
                           ["Invalid user_input strings with digits , and as", "AS 0,1", None],
                           ["Invalid user_input strings with digits multiple ,", "0,1,", None],
                           ["Invalid user_input strings with digits multiple ,", "0,1,3,4", None],
                           ["Invalid user_input with negatives", "0,-1", None],
                           ["Invalid user_input without comma,", "0 1", None],
                           ["Invalid user_input large numbers", "55555555,44444444", None],
                           ["valid", "0,1", (0, 1)],
                           ["valid", "40,100", (40, 100)],
                           ["valid whitespace test", "    0,1    ",  (0, 1)],
                           ["valid whitespace test 2 ", "    0 ,   1    ", (0, 1)]])
    def test_gen_board_output_and_updates(self, name: str, user_input: str, result: bool):
        player = HumanPlayer("X", None)
        self.assertEqual(player.process_input(user_input), result)

    def test_user_input_valid_input(self):
        board = Board()
        player = HumanPlayer("X", board)
        player.get_input = MagicMock(return_value="0,1")
        player.make_move()
        self.assertEquals(board.get_moves, [(1, 0, 'X')])

    def test_user_input_invalid_then_valid_input(self):
        board = Board()
        player = HumanPlayer("X", board)
        player.get_input = Mock()
        player.get_input.side_effect = ["A,3", "4,4", "0,1"]
        player.make_move()
        self.assertEquals(board.get_moves, [(1, 0, "X")])

    #######################################
    #  Random Computer Player Unit Test   #
    #######################################
    def test_random_computer_player(self):
        board = Board()
        player = RandomComputerPlayer("X", board)
        player.make_move()
        move = board.get_moves[0]
        self.assertEquals(move[2], "X")
        self.assertTrue(0 <= move[0] <= 2)
        self.assertTrue(0 <= move[1] <= 2)

    #######################################
    #  Minmax Computer Player Unit Test   #
    #######################################
    def test_minmax_computer_player(self):
        board = Board()
        player = MinMaxComputerPlayer("O", board)
        board.update(0, 0)
        player.make_move()
        computer_move = board.get_moves[1]
        self.assertEquals(computer_move, (1, 1, "O"))



    #############################
    #      Unit Board Test      #
    #############################
    @parameterized.expand([["0,0 X", 3, 0, 0, "X", '  0 1 2\n0 X| | \n  -----\n1  | | \n  -----\n2  | | \n'],
                           ["1,1 O", 3, 1, 1, "O", '  0 1 2\n0  | | \n  -----\n1  |O| \n  -----\n2  | | \n'],
                           ["2,2 P", 3, 2, 2, "P", '  0 1 2\n0  | | \n  -----\n1  | | \n  -----\n2  | |P\n'],
                           ["3,3 W", 4, 3, 3, "W",
                            '  0 1 2 3\n0  | | | \n  ------\n1  | | | \n  ------\n2  | | | \n  ------\n3  | | |W\n']])
    def test_gen_board_output_and_updates(self, name: str, s: int, x: int, y: int, marker: str, result: str):
        board = Board(size=s, play_order=[marker, "O"])
        board.update(x, y)
        self.assertEqual(board.gen_board_output(), result)

    @parameterized.expand([["valid_move 0 0", 3, 0, 0, (True, 'good')],
                           ["valid_move 1 1", 3, 1, 1, (True, 'good')],
                           ["invalid_move -1 0", 3, -1, 0, (False, "x value '-1' is less then zero ")],
                           ["invalid_move 0 -1", 3, 0, -1, (False, "y value '0' is less then zero ")],
                           ["invalid_move 0 3", 3, 0, 3, (False, "y value '3' is greater then board size 2")],
                           ["invalid_move", 3, 3, 0, (False, "x value '3' is greater then board size 2")],
                           ["invalid_move", 4, 4, 3, (False, "x value '4' is greater then board size 3")],
                           ["invalid_move", 4, 3, 4, (False, "y value '4' is greater then board size 3")],
                           ["valid_move", 4, 3, 3, (True, 'good')]])
    def test_board_is_valid_move(self, name: str, s: int, x: int, y: int,  result: Tuple[bool, str]):
        board = Board(size=s)
        self.assertEqual(board.is_valid_location(x, y), result)

    def test_board_is_valid_move_existing_marker(self):
        board = Board()
        board.update(1, 1)
        self.assertEqual(board.is_valid_location(1, 1), (False, "it is already filled with X"))

    # In a 3x3 tic tac toe board there is 8 possible way of winning 3 horizontal, 3 vertical and 2 diagonal
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
                           ["twin game 1", 3, 3, [["X", "X", "O"],
                                                  ["O", "O", "X"],
                                                  ["X", "O", "X"]], None],
                           ["twin game 2", 3, 3, [["X", "X", "O"],
                                                  ["O", "O", "X"],
                                                  ["X", "O", "X"]], None],
                           ["twin game 3", 3, 3, [["X", "O", "O"],
                                                  ["O", "X", "X"],
                                                  ["O", "X", "O"]], None],
                           ["twin game 4", 3, 3, [["X", "O", "O"],
                                                  ["O", "X", "X"],
                                                  ["X", "X", "O"]], None],
                           ["twin game 5", 3, 3, [["X", "O", "X"],
                                                  ["O", "O", "X"],
                                                  ["X", "X", "O"]], None],
                           ["twin game 6", 3, 3, [["O", "X", "O"],
                                                  ["O", "X", "X"],
                                                  ["X", "O", "X"]], None],
                           ])
    def test_board_winner(self, name: str, s: int, wc: int, board_setup: List[List],  result: str):
        board = Board(size=s, win_count=wc)
        board._board = board_setup
        self.assertEqual(board.winner(), result)

    @parameterized.expand([["empty board", 3, [[None, None, None],
                                               [None, None, None],
                                               [None, None, None]], False],
                           ["semi board", 3, [["X", None, "X"],
                                              ["X", "O", None],
                                              ["O", None, "X"]], False],

                           ["full board", 3, [["X", "O", "X"],
                                              ["X", "O", "O"],
                                              ["O", "O", "X"]], True],
                           ])
    def test_board_is_board_full(self, name: str, s: int, board_setup: List[List], result: str):
        board = Board(size=s)
        board._board = board_setup
        self.assertEqual(board.is_board_full(), result)

    def test_board_undo(self):
        board = Board()
        board.update(1, 1)
        self.assertEquals(board.get_moves, [(1, 1, "X")])
        board.undo()
        self.assertEquals(board.get_moves, [])
        board.undo()    # Check what happens when you undo there is nothing to undo
        self.assertEquals(board.get_moves, [])

    # Testing the board update state as updates occur
    def test_board_update_state_winner(self):
        board = Board()
        board.update(1, 1)  # X
        self.assertEquals(board.get_state, State.INPLAY)
        board.update(0, 1)  # O
        self.assertEquals(board.get_state, State.INPLAY)
        board.update(0, 0)  # X
        self.assertEquals(board.get_state, State.INPLAY)
        board.update(0, 2)  # 0
        self.assertEquals(board.get_state, State.INPLAY)
        board.update(2, 2)  # X
        self.assertEquals(board.get_state, State.WINNER)
        self.assertEquals(board.get_winner, "X")

    def test_board_update_state_draw(self):
        board = Board()

        """ Board will look like this:
          0 1 2
        0 X|O|X
          -----
        1 X|O|X
          -----
        2 O|O|X
        """
        moves = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (2, 0),  (2, 1), (1, 2)]
        for x, y in moves:
            board.update(x, y)  # X
            self.assertEquals(board.get_state, State.INPLAY)
        board.update(2, 2)
        self.assertEquals(board.get_state, State.DRAW)
        self.assertEquals(board.get_winner, None)

    def test_4_by_4_board(self):
        board = Board(size=4)
        self.assertEquals(board.get_size, 4)
        self.assertEquals(board.gen_board_output(),
                          '  0 1 2 3\n0  | | | \n  ------\n1  | | | \n  ------\n2  | | | \n  ------\n3  | | | \n')

if __name__ == '__main__':
    unittest.main()
