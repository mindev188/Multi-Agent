from datetime import datetime
from typing import Optional


class Board:
    def __init__(self, owner: str, title: str, content: str):
        self.id: Optional[int] = None
        self.owner = owner
        self.title = title
        self.content = content
        self.created_at: datetime = datetime.utcnow()
        self.updated_at: datetime = datetime.utcnow()

    def update_board(self, title: str, content: str):
        self.title = title
        self.content = content