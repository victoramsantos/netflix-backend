import os

from src.library.database.Mongo import Mongo


class VotesRepository:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_INITDB_DATABASE")
        )
        self.__ranking = os.getenv("MONGO_INITDB_DATABASE")

    def get_votes_by(self, movie_id):
        return self.__mongo.find_by(
            collection=self.__ranking,
            query={
                "movieId": movie_id
            }
        )

    def list_votes(self):
        return [elem for elem in self.__mongo.find_all(self.__ranking)]

    def post_vote(self, movie_id: int):
        if self.get_votes_by(movie_id):
            self.__mongo.update_by(
                collection=self.__ranking,
                query={
                    "movieId": movie_id
                },
                obj={
                    "$inc": {
                        "votes": 1
                    }
                }
            )
        else:
            self.__mongo.insert_one(
                collection=self.__ranking,
                elem={
                    "movieId": movie_id,
                    "votes": 1
                }
            )
