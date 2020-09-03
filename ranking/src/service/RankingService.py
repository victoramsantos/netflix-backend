from src.repository.MoviesRepository import MoviesRepository
from src.repository.VotesRepository import VotesRepository


class RankingService:
    def __init__(self, votes_repository: VotesRepository, movies_repository: MoviesRepository):
        self.__votes_repository = votes_repository
        self.__movies_repository = movies_repository

    def ranking_by_gender(self, gender: str):
        movies = self.__movies_repository.get_movies_by_gender(gender)
        ranking = [self.__get_votes(movie) for movie in movies]

        return sorted(ranking, key=lambda k: k['votes'], reverse=True)

    def __get_votes(self, movie):
        votes = self.__votes_repository.get_votes_by(movie["movieId"])
        if not votes:
            votes = {
                "movieId": movie["movieId"],
                "votes": 0
            }
        votes["name"] = movie["name"]
        return votes
