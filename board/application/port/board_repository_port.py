from abc import ABC, abstractmethod

from board.domain.board import Board


class BoardRepositoryPort(ABC):

    @abstractmethod
    def create_board(self, board: Board) -> Board:
        pass