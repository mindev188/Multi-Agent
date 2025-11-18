from datetime import datetime

from pydantic import BaseModel


class AccountResponse(BaseModel):
    id: int
    email: str
    nickname: str
    created_at: datetime
    updated_at: datetime