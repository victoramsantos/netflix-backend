from src.repository.WatchedRepository import WatchedRepository


class WatchedService:
    def __init__(self, watched_repository: WatchedRepository):
        self.__watched_repository = watched_repository

    def list_watched(self):
        return self.__watched_repository.list_watched()

    def post_watched(self, user_id: int, movie_id: int):
        self.__watched_repository.post_watched(
            user_id=user_id,
            movie_id=movie_id
        )

    def get_watched(self, user_id: int):
        return self.__watched_repository.get_watched(
            user_id=user_id
        )
