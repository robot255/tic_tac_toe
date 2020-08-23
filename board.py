from typing import Tuple, List, Optional
from enum import Enum


class State(Enum):
    DRAW = 0
    INPLAY = 2
    WINNER = 1


class Board:
    # To Do provide the play order in
    def __init__(self, size=3, win_count=3, play_order=None):
        if play_order is None:
            play_order = ["X", "O"]
        self._size = size
        self._win_count = win_count
        self._board = [[None for _ in range(self._size)] for _ in range(self._size)]
        self._state = State.INPLAY
        self._winner = None
        self._moves = []
        self._play_order = play_order

    @property
    def get_size(self) -> int:
        return self._size

    @property
    def get_state(self) -> State:
        return self._state

    @property
    def get_moves(self) -> List[Tuple[int, int, str]]:
        return self._moves

    @property
    def get_winner(self) -> str:
        return self._winner

    def is_valid_location(self, x, y) -> Tuple[bool, str]:
        # Since python lazy evaluates boolean expressions have to check things separately
        # https://docs.python.org/2/reference/expressions.html#boolean-operations
        if 0 > x:
            return False, f"x value '{x}' is less then zero "
        if x > (self._size - 1):
            return False, f"x value '{x}' is greater then board size {self._size - 1}"
        if 0 > y:
            return False, f"y value '{x}' is less then zero "
        if y > (self._size - 1):
            return False, f"y value '{y}' is greater then board size {self._size - 1}"
        if self._board[x][y] is not None:
            return False, f"it is already filled with {self._board[x][y]}"
        return True, "good"

    # Need to test method
    def is_board_full(self):
        return len(self.get_possible_moves()) == 0

    def undo(self):
        if len(self._moves) == 0:
            return

        x, y, _ = self._moves.pop()
        self._board[x][y] = None
        self.update_board_state()

    def get_possible_moves(self):
        p_moves = []
        for x in range(self._size):
            for y in range(self._size):
                if self._board[x][y] is None:
                    p_moves.append((x, y))
        return p_moves

    def update_board_state(self):
        winner = self.winner()
        if winner:
            self._state = State.WINNER
            self._winner = winner
        elif winner is None and self.is_board_full():
            self._state = State.DRAW
            self._winner = None
        else:
            self._state = State.INPLAY
            self._winner = None

    def update(self, x: int, y: int) -> None:
        marker = self._play_order[len(self._moves) % len(self._play_order)]
        self._board[x][y] = marker
        self._moves.append((x, y, marker))
        self._winner = self.winner()
        self.update_board_state()

    def winner(self) -> Optional[str]:
        for x in range(self._size):  # rows
            for y in range(self._size):  # columns
                marker = self._board[x][y]
                if marker is None:
                    continue  # No marker skip checks

                # Horizontal
                if x + self._win_count <= self._size:
                    horizontal_win: bool = True
                    for i in range(1, self._win_count):
                        if self._board[x + i][y] is None or self._board[x + i][y] != marker:
                            horizontal_win = False
                            break
                    if horizontal_win:
                        return marker

                # Vertical
                if y + self._win_count <= self._size:
                    vertical_win: bool = True
                    for i in range(1, self._win_count):
                        if self._board[x][y + i] is None or self._board[x][y + i] != marker:
                            vertical_win = False
                            break
                    if vertical_win:
                        return marker

                    # Diagonal
                    if x + self._win_count <= self._size:
                        vertical_right_win: bool = True
                        for i in range(1, self._win_count):
                            if self._board[x + i][y + i] is None or self._board[x + i][y + i] != marker:
                                vertical_right_win = False
                                break
                        if vertical_right_win:
                            return marker

                    if x - (self._win_count - 1) >= 0:
                        vertical_left_win: bool = True
                        for i in range(1, self._win_count):
                            if self._board[x - i][y + i] is None or self._board[x - i][y + i] != marker:
                                vertical_left_win = False
                                break
                        if vertical_left_win:
                            return marker
        return None

    def gen_board_output(self) -> str:
        output = "  " + " ".join([str(x) for x in range(self._size)]) + "\n"

        for i, row in enumerate(self._board):
            output += f"{i} "
            # Replace the None with blank spaces
            output += "|".join([" " if x is None else x for x in row]) + "\n"
            if i + 1 != self._size:
                output += "  " + "-" * (self._size + 2) + "\n"
        return output
