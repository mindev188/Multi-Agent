from fastapi import APIRouter, HTTPException, Cookie

from account.adapter.input.web.request.update_nickname_request import UpdateNicknameRequest
from account.adapter.input.web.response.account_response import AccountResponse
from account.application.usecase.account_usecase import AccountUseCase
from account.infrastructure.repository.account_repository_impl import AccountRepositoryImpl
from config.redis_config import get_redis
from social_oauth.application.usecase.google_oauth2_usecase import GoogleOAuth2UseCase
from social_oauth.infrastructure.service.google_oauth2_service import GoogleOAuth2Service

service = GoogleOAuth2Service
account_router = APIRouter()
account_usecase = AccountUseCase.getInstance()
google_usecase = GoogleOAuth2UseCase(service)

redis_client = get_redis()

@account_router.patch("/update/nickname")
def update_nickname(request: UpdateNicknameRequest, session_id: str | None = Cookie(None)):
    print("[DEBUG] /update/nickname session id : ", session_id)
    exists = redis_client.exists(session_id)
    if not exists :
        raise HTTPException(status_code=404, detail="login please")

    data = redis_client.hgetall(session_id)
    email = data.get("email")

    rows = account_usecase.update_nickname(email, request.nickname)
    if rows <= 0:
        raise HTTPException(status_code=404, detail="account update fail")
    return {"message": "success account update!"}