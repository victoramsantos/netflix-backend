from src.repository.MoviesRepository import MoviesRepository


class MoviesService:
    def __init__(self, movies_repository: MoviesRepository):
        self.__movies_repository = movies_repository

    def add_movie(self, movie: dict):
        self.__movies_repository.add_movie(movie)

    def list_movies(self):
        return self.__movies_repository.list_movies()
