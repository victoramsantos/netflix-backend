from flask import Blueprint, request

from src.controller import support_service
from src.controller.UtilController import UtilController
from src.library.logger.Logger import Logger

support_controller = Blueprint('SupportController', __name__)


class SupportController:
    @staticmethod
    @support_controller.route('/support/<int:user_id>', methods=['POST'])
    def post_support(user_id: int):
        response: dict
        status_code: int = 204
        try:
            Logger.info(f"post_support")
            message = request.json
            response = support_service.call_support(user_id, message)
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)
