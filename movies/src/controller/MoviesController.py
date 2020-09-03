import json

from flask import Blueprint, request

from src.controller import service
from src.controller.UtilController import UtilController
from src.library.logger.Logger import Logger

movies_controller = Blueprint('MoviesController', __name__)


class MoviesController:
    @staticmethod
    @movies_controller.route('/movies', methods=['POST'])
    def add_movie():
        response: dict
        status_code: int = 204
        try:
            movie = request.json
            Logger.info(f"add_movie: movie={movie['name']}")
            response = service.add_movie(
                movie=movie
            )
        except Exception as exception:
            Logger.error(str(exception))
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @movies_controller.route('/movies', methods=['GET'])
    def list_movies():
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"list_movies")
            response = service.list_movies()
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @movies_controller.route('/movies/<int:movie_id>', methods=['GET'])
    def filter_movie(movie_id: int):
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"filter_movie - movie_id:{movie_id}")
            response = service.filter_movie(movie_id)
            if not response:
                status_code = 404
                response = {}
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @movies_controller.route('/movies/gender/<string:gender>', methods=['GET'])
    def filter_movies_by_gender(gender: str):
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"filter_movies_by_gender - gender:{gender}")
            response = service.filter_movies_by_gender(gender)
            if not response:
                status_code = 404
                response = {}
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @movies_controller.route('/movies/', methods=['GET'])
    def filter_movies_by_query_string():
        response: dict
        status_code: int = 200
        try:
            query = request.args["q"]
            Logger.info(f"filter_movies_by_query_string - query:{query}")
            response = service.filter_movies_by_query_string(query)
            if not response:
                status_code = 404
                response = {}
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)