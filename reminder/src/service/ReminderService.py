from src.repository.ReminderRepository import ReminderRepository


class ReminderService:
    def __init__(self, reminder_repository: ReminderRepository):
        self.__reminder_repository = reminder_repository

    def list_reminder(self):
        return self.__reminder_repository.list_reminder()

    def post_reminder(self, user_id: int, movie_id: int):
        self.__reminder_repository.post_reminder(
            user_id=user_id,
            movie_id=movie_id
        )

    def get_reminder(self, user_id: int):
        return self.__reminder_repository.get_reminder(
            user_id=user_id
        )