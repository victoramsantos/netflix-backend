import os

from src.library.database.Mongo import Mongo


class ReminderRepository:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_INITDB_DATABASE")
        )
        self.__reminder = os.getenv("MONGO_REMINDER_COLLECTION")

    def list_reminder(self):
        return [elem for elem in self.__mongo.find_all(self.__reminder)]

    def post_reminder(self, user_id: int, movie_id: int):
        self.__mongo.push_element(
            collection=self.__reminder,
            query={
                "userId": user_id
            },
            obj={
                "movies": movie_id
            }
        )

    def get_reminder(self, user_id: int):
        return self.__mongo.find_by(
            collection=self.__reminder,
            query={
                "userId": user_id
            }
        )
