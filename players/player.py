from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, marker: str):
        self._marker = marker

    def get_marker(self) -> str:
        return self._marker

    @abstractmethod
    def make_move(self) -> None:
        pass
