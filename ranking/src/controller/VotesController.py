from flask import Blueprint, request

from src.controller import vote_service
from src.controller.UtilController import UtilController
from src.library.logger.Logger import Logger

votes_controller = Blueprint('VotesController', __name__)


class VotesController:
    @staticmethod
    @votes_controller.route('/votes', methods=['GET'])
    def list_votes():
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"list_votes")
            response = vote_service.list_votes()
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @votes_controller.route('/votes/<int:movie_id>', methods=['GET'])
    def get_votes_by(movie_id: int):
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"get_votes_by: movie_id={movie_id}")
            response = vote_service.get_votes_by(movie_id)
            if not response:
                status_code = 404
                response = {}
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @votes_controller.route('/votes/<int:movie_id>/like', methods=['POST'])
    def post_vote(movie_id: int):
        response: dict = {}
        status_code: int = 204
        try:
            Logger.info(f"post_vote: movie_id={movie_id}")
            vote_service.post_vote(movie_id)
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)