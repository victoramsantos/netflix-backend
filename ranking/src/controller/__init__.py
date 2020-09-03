from src.repository.MoviesRepository import MoviesRepository
from src.repository.VotesRepository import VotesRepository
from src.service.RankingService import RankingService
from src.service.VotesService import VotesService

vote_service = VotesService(
    votes_repository=VotesRepository()
)

ranking_service = RankingService(
    votes_repository=VotesRepository(),
    movies_repository=MoviesRepository()
)
