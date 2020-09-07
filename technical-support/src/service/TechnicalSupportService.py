from src.repository.TechnicalSupportRepository import TechnicalSupportRepository


class TechnicalSupportService:
    def __init__(self, support_repository: TechnicalSupportRepository):
        self.__support_repository = support_repository

    def call_support(self, user_id: int, message: str):
        return self.__support_repository.call_support(user_id, message)
