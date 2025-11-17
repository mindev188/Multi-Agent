from typing import List

from fastapi import APIRouter, HTTPException

from anonymous_board.adapter.input.web.request.create_anonymous_board_request import CreateAnonymousBoardRequest
from anonymous_board.adapter.input.web.request.update_anonymous_board_request import UpdateAnonymousBoardRequest
from anonymous_board.adapter.input.web.response.anonymous_board_response import AnonymousBoardResponse
from anonymous_board.application.usecase.anonymous_board_usecase import AnonymousBoardUseCase
from anonymous_board.domain.anonymous_board import AnonymousBoard
from anonymous_board.infrastructure.repository.anonymous_board_repository_impl import AnonymousBoardRepositoryImpl

anonymous_board_router = APIRouter()
usecase = AnonymousBoardUseCase(AnonymousBoardRepositoryImpl())

@anonymous_board_router.post("/create", response_model=AnonymousBoardResponse)
def create_board(request: CreateAnonymousBoardRequest):
    board = usecase.create_board(request.title, request.content)
    return AnonymousBoardResponse(
        id=board.id,
        title=board.title,
        content=board.content,
        created_at=board.created_at,
        updated_at=board.updated_at,
    )

@anonymous_board_router.get("/list", response_model=List[AnonymousBoardResponse])
def list_boards():
    boards = usecase.list_boards()
    return [
        AnonymousBoardResponse(
            id=b.id,
            title=b.title,
            content=b.content,
            created_at=b.created_at,
            updated_at=b.updated_at,
        ) for b in boards
    ]

@anonymous_board_router.get("/read/{board_id}", response_model=AnonymousBoardResponse)
def get_board(board_id: int):
    board = usecase.get_board(board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return AnonymousBoardResponse(
        id=board.id,
        title=board.title,
        content=board.content,
        created_at=board.created_at,
        updated_at=board.updated_at,
    )

@anonymous_board_router.delete("/delete/{board_id}")
def delete_board(board_id: int):
    success = usecase.delete_board(board_id)
    if not success:
        raise HTTPException(status_code=404, detail="Board not found")
    return {"message": "Deleted successfully"}

@anonymous_board_router.put("/update/{board_id}")
def update_board(request: UpdateAnonymousBoardRequest, board_id: int):
    anonymous_board = AnonymousBoard(request.title, request.content)
    anonymous_board.id = board_id
    rows = usecase.update_board(anonymous_board)
    if rows <= 0:
        raise HTTPException(status_code=404, detail="Board not found")
    return {"message": "Updated successfully"}
