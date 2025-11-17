from pydantic import BaseModel


class UpdateAnonymousBoardRequest(BaseModel):
    title: str
    content: str
