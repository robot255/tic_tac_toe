from typing import List

from board import Board, State
from players.human_player import HumanPlayer
from players.random_computer import RandomComputerPlayer
from players.minimax_computer import MinMaxComputerPlayer


class TicTacToe:

    def __init__(self, board_size: int = 3, win_count: int = 3, players: List[str] = ['human', 'minimax']):
        if len(players) != 2:
            raise Exception("Currently unable to handle more then 2 players")

        player_markers = ["X", "O"]

        self._board = Board(size=board_size, win_count=win_count, play_order=player_markers)

        self._players = []
        for i, player in enumerate(players):
            if player == "human":
                self._players.append(HumanPlayer(player_markers[i], self._board))
            elif player == "random":
                self._players.append(RandomComputerPlayer(player_markers[i], self._board))
            elif player == "minimax":
                self._players.append(MinMaxComputerPlayer(player_markers[i], self._board))

    def start_game(self) -> None:
        turn = 0
        while self._board.get_state == State.INPLAY:
            player = turn % len(self._players)
            self._players[player].make_move()
            turn += 1
            print(self._board.gen_board_output())

        if self._board.get_state == State.DRAW:
            print("Tie Game")
        else:
            print(f"Winner is {self._board.get_winner}")





