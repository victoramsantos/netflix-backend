from src.repository.VotesRepository import VotesRepository


class VotesService:
    def __init__(self, votes_repository: VotesRepository):
        self.__votes_repository = votes_repository

    def get_votes_by(self, movie_id: int):
        return self.__votes_repository.get_votes_by(movie_id)

    def list_votes(self):
        return self.__votes_repository.list_votes()

    def post_vote(self, movie_id: int):
        self.__votes_repository.post_vote(movie_id)