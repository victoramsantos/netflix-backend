import os

import requests


class MoviesRepository:
    def __init__(self):
        self.__host = os.getenv("MOVIES_HOST")
        self.__port = os.getenv("MOVIES_PORT")
        self.__room_url = f"http://{self.__host}:{self.__port}"

    def get_movies_by_gender(self, gender: str):
        response = requests.get(
            url=f"{self.__room_url}/movies/gender/{gender}"
        )

        if response.status_code == 404:
            raise Exception("Gender not found")
        return response.json()
