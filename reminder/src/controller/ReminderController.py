from flask import Blueprint

from src.controller import reminder_service
from src.controller.UtilController import UtilController
from src.library.logger.Logger import Logger

reminder_controller = Blueprint('ReminderController', __name__)


class ReminderController:
    @staticmethod
    @reminder_controller.route('/reminder', methods=['GET'])
    def list_reminder():
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"list_reminder")
            response = reminder_service.list_reminder()
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @reminder_controller.route('/reminder/<int:user_id>/<int:movie_id>', methods=['POST'])
    def post_reminder(user_id: int, movie_id: int):
        response: dict = {}
        status_code: int = 204
        try:
            Logger.info(f"post_reminder: user_id:{user_id} movie_id={movie_id}")
            reminder_service.post_reminder(user_id, movie_id)
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @reminder_controller.route('/reminder/<int:user_id>', methods=['GET'])
    def get_reminder(user_id: int):
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"get_reminder: user_id={user_id}")
            response = reminder_service.get_reminder(user_id)
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)