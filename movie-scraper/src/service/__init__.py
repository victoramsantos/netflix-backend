from src.repository.DatasetRepository import DatasetRepository
from src.repository.MoviesRepository import MoviesRepository
from src.service.ScraperService import ScraperService

movies_repository = MoviesRepository()
dataset_repository = DatasetRepository()

scraper_service = ScraperService(
    movies_repository=movies_repository,
    dataset_repository=dataset_repository
)