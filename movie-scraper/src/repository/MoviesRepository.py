import json
import os

import requests


class MoviesRepository:
    def __init__(self):
        self.__host = os.getenv("MOVIES_HOST")
        self.__port = os.getenv("MOVIES_PORT")
        self.__movies_url = f"http://{self.__host}:{self.__port}"

    def add_movie(self, movie: dict):
        requests.post(
            url=f"{self.__movies_url}/movies",
            json=json.dumps(movie)
        )
