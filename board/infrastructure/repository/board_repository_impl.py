from sqlalchemy.orm import Session

from board.application.port.board_repository_port import BoardRepositoryPort
from board.domain.board import Board
from board.infrastructure.orm.board_orm import BoardORM
from config.database.session import get_db_session


class BoardRepositoryImpl(BoardRepositoryPort):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'db'):
            self.db: Session = get_db_session()

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def create_board(self, board: Board) -> Board:
        orm_board = BoardORM(
            owner = board.owner,
            title = board.title,
            content = board.content
        )
        self.db.add(orm_board)
        self.db.commit()
        self.db.refresh(orm_board)

        return board