from flask import Blueprint

from src.controller import watched_service
from src.controller.UtilController import UtilController
from src.library.logger.Logger import Logger

watched_controller = Blueprint('WatchedController', __name__)


class WatchedController:
    @staticmethod
    @watched_controller.route('/watched', methods=['GET'])
    def list_watched():
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"list_watched")
            response = watched_service.list_watched()
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @watched_controller.route('/watched/<int:user_id>/<int:movie_id>', methods=['POST'])
    def post_watched(user_id: int, movie_id: int):
        response: dict = {}
        status_code: int = 204
        try:
            Logger.info(f"post_watched: user_id:{user_id} movie_id={movie_id}")
            watched_service.post_watched(user_id, movie_id)
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @watched_controller.route('/watched/<int:user_id>', methods=['GET'])
    def get_watched(user_id: int):
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"get_watched: user_id={user_id}")
            response = watched_service.get_watched(user_id)
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)