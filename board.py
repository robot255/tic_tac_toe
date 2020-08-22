class Board():

    def __init__(self, size=3, win_count=3):
        self._size = size
        self._win_count = win_count
        self._board = [[None for _ in range(self._size)] for _ in range(self._size)]

    def is_valid_location(self, x, y):
        # Since python lazy evaluates boolean expressions have to check things separately
        # https://docs.python.org/2/reference/expressions.html#boolean-operations
        if 0 > x:
            return False
        if x > (self._size - 1):
            return False
        if 0 > y:
            return False
        if y > (self._size - 1):
            return False
        if self._board[x][y] is not None:
            return False
        return True

    # Need to test method
    def is_board_full(self):
        for x in range(self._size):
            for y in range(self._size):
                if self._board[x][y] is None:
                    return False
        return True

    # where should the error checking exist in the update method or the tic tac toe
    def update(self, x: int, y: int, marker: str) -> None:
        self._board[x][y] = marker

    def winner(self, ) -> str:
        for x in range(self._size):  # rows
            for y in range(self._size):  # columns
                marker = self._board[x][y]
                if marker is None:
                    continue #No marker skip checks

                # Horizonital
                if x + self._win_count <= self._size:
                    horizontal_win: bool = True
                    for i in range(1, self._win_count):
                        if self._board[x+i][y] is None or self._board[x+i][y] != marker:
                            horizontal_win = False
                            break
                    if horizontal_win:
                        return marker

                # Vertical
                if y + self._win_count <= self._size:
                    vertical_win: bool = True
                    for i in range(1, self._win_count):
                        if self._board[x][y+i] is None or self._board[x][y+i] != marker:
                            vertical_win = False
                            break
                    if vertical_win:
                        return marker

                    # Diagonal
                    if x + self._win_count <= self._size:
                        vertical_right_win: bool = True
                        for i in range(1, self._win_count):
                            if self._board[x+i][y+i] is None or self._board[x+i][y+i] != marker:
                                vertical_right_win = False
                                break
                        if vertical_right_win:
                            return marker

                    if x - (self._win_count - 1) >= 0:
                        vertical_left_win: bool = True
                        for i in range(1, self._win_count):
                            if self._board[x-i][y+i] is None or self._board[x-i][y+i] != marker:
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