import os

from src.library.logger.Logger import Logger
from src.repository.DatasetRepository import DatasetRepository
from src.repository.MoviesRepository import MoviesRepository


class ScraperService:
    def __init__(self,
                 movies_repository: MoviesRepository,
                 dataset_repository: DatasetRepository):
        self.__movies_repository = movies_repository
        self.__dataset_repository = dataset_repository

        self.__max_movies = int(os.getenv("MAX_MOVIES"))
        if self.__max_movies > 1_000:
            raise Exception("We are limited to 1,000 movies")

    def process_dataset(self):
        movies_count = 0
        for movie in self.__dataset_repository.iterate_over_movies():
            if movies_count > self.__max_movies:
                break
            self.__movies_repository.add_movie(movie)
            Logger.info(f"Sent movie {movies_count+1}/{self.__max_movies} - {movie['name']}")
            movies_count += 1
