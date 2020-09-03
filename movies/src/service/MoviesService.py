from src.repository.MoviesRepository import MoviesRepository


class MoviesService:
    def __init__(self, movies_repository: MoviesRepository):
        self.__movies_repository = movies_repository

    def add_movie(self, movie: dict):
        self.__movies_repository.add_movie(movie)

    def list_movies(self):
        return self.__movies_repository.list_movies()

    def filter_movie(self, movie_id: int):
        return self.__movies_repository.filter_movie(movie_id)

    def filter_movies_by_gender(self, gender: str):
        return self.__movies_repository.filter_movies_by_gender(gender)

    def filter_movies_by_query_string(self, query: str):
        return self.__movies_repository.filter_movies_by_query_string(query)