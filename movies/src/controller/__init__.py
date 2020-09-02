from src.repository.MoviesRepository import MoviesRepository
from src.service.MoviesService import MoviesService

service = MoviesService(
    movies_repository=MoviesRepository()
)
