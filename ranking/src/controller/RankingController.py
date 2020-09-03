from flask import Blueprint

from src.controller import ranking_service
from src.controller.UtilController import UtilController
from src.library.logger.Logger import Logger

ranking_controller = Blueprint('RankingController', __name__)


class RankingController:
    @staticmethod
    @ranking_controller.route('/ranking/gender/<string:gender>', methods=['GET'])
    def ranking_by_gender(gender: str):
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"ranking_by_gender - gender={gender}")
            response = ranking_service.ranking_by_gender(gender)
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)
