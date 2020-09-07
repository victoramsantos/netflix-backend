from src.repository.SupportRepository import SupportRepository


class SupportService:
    def __init__(self, support_repository: SupportRepository):
        self.__support_repository = support_repository

    def call_support(self, user_id: int, message: str):
        return self.__support_repository.call_support(user_id, message)
