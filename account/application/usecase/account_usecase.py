from account.domain.account import Account
from account.infrastructure.repository.account_repository_impl import AccountRepositoryImpl
from social_oauth.adapter.input.web.request.get_access_token_request import GetAccessTokenRequest
from social_oauth.infrastructure.service.google_oauth2_service import GoogleOAuth2Service


class AccountUseCase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.repo = AccountRepositoryImpl.getInstance()
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'service'):
            self.service = GoogleOAuth2Service


    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create_or_get_account(self, email: str, nickname: str | None):
        account = self.repo.find_by_email(email)
        if account:
            return account

        if not nickname:
            total = self.repo.count()
            nickname = f"anonymous{total + 1}"

        account = Account(email=email, nickname=nickname)
        return self.repo.save(account)

    def update_nickname(self, email, nickname):
        '''
        1. email 일치 계정 존재 여부 확인
        2. 계정 update
        '''
        account = self.repo.find_by_email(email)
        if not account:
            return -1

        return self.repo.update_by_email(email, nickname)
