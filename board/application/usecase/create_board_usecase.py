from board.domain.board import Board
from board.infrastructure.repository.board_repository_impl import BoardRepositoryImpl


class CreateBoardUsecase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.repo = BoardRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create_board(self, board: Board):

        return self.repo.create_board(board)