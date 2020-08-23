import argparse

from tic_tac_toe import TicTacToe

parser = argparse.ArgumentParser(description="Tic Tac Toe Game")
parser.add_argument('-s', "--size", type=str, help="size of the game board", default=3)
parser.add_argument('-wc', "--win_count", type=str, help="number markers in a row required for a win", default=3)
parser.add_argument('-p1', "--player1", type=str, help="human, random, or minimax", default="human")
parser.add_argument('-p2', "--player2", type=str, help="human, random, or minimax", default="minimax")

args = parser.parse_args()

TicTacToe(args.size, args.win_count, [args.player1, args.player2]).start_game()