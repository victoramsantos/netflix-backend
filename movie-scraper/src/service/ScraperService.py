from src.repository.DatasetRepository import DatasetRepository
from src.repository.MoviesRepository import MoviesRepository


class ScraperService:
    def __init__(self,
                 movies_repository: MoviesRepository,
                 dataset_repository: DatasetRepository):
        self.__movies_repository = movies_repository
        self.__dataset_repository = dataset_repository

    def process_dataset(self):
        for movie in self.__dataset_repository.iterate_over_movies():
            print(movie)
