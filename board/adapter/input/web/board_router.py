from fastapi import APIRouter, Cookie, HTTPException

from board.adapter.input.web.request.create_board_request import CreateBoardRequest
from board.application.usecase.create_board_usecase import CreateBoardUsecase
from board.domain.board import Board
from config.redis_config import get_redis

board_router = APIRouter()
redis_client = get_redis()

usecase = CreateBoardUsecase.getInstance()

@board_router.post("/create")
def create_board(request: CreateBoardRequest, session_id: str | None = Cookie(None)):
    exists = redis_client.exists(session_id)
    if not exists :
        raise HTTPException(status_code=404, detail="login please")

    data = redis_client.hgetall(session_id)
    owner = data.get("email")

    # board create
    board = Board(owner, request.title, request.content)
    if usecase.create_board(board) is None:
       raise HTTPException(status_code=404, detail="create board fail")

    return {"message":"create success! " + board.title}