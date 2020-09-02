import os

from src.library.database.Mongo import Mongo


class MoviesRepository:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_INITDB_DATABASE")
        )
        self.__movies = os.getenv("MONGO_INITDB_DATABASE")

    def add_movie(self, movie: dict):
        self.__mongo.insert_one(
            collection=self.__movies,
            elem=movie
        )

    def list_movies(self):
        return [elem for elem in self.__mongo.find_all(self.__movies)]