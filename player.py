class player():

    def __init__(self, marker: str, is_human: bool):
        self._marker = marker
        self._is_human = is_human

    def get_marker(self) -> str:
        return self._marker

    def is_human(self) -> bool:
        return self._is_human

    def get_move(self):
        pass