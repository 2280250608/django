"""
File in which we have the middleware for Django for Authenticating API requests
"""
import json
import jwt
import logging
from environs import Env
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

# Initialize logger
logger = logging.getLogger(__name__)

# Get JWT secret key
SECRET_KEY = "Bearer hamed123456789izadyfar@"


def create_response(request_id, code, message):
    """
    Function to create a response to be sent back via the API
    :param request_id:Id fo the request
    :param code:Error Code to be used
    :param message:Message to be sent via the APi
    :return:Dict with the above given params
    """

    try:
        req = str(request_id)
        data = {"data": message, "code": int(code), "request_id": req}
        return data
    except Exception as creation_error:
        logger.error(f'create_response:{creation_error}')


class AuthMiddleware(MiddlewareMixin):
    """
    Custom Middleware Class to process a request before it reached the endpoint
    """

    def process_request(self, request):

        """
        Custom middleware handler to check authentication for a user with JWT authentication
        :param request: Request header containing authorization tokens
        :type request: Django Request Object
        :return: HTTP Response if authorization fails, else None
        """

        token = request.headers.get('authorization', None)
        print(f"request received for endpoint {str(request.path)} -> {token}")

        # If token Exists
        if token:
            try:
                if token != SECRET_KEY:
                    response = create_response("", 4001, {"message": "Authorization has failed, Please send valid "
                                                                     "token."})
                    return HttpResponse(json.dumps(response), status=401)
            except BaseException as e:
                print(e)

        else:
            response = create_response(
                "", 4001, {"message": "Authorization not found, Please send valid token in headers"}
            )
            logger.info(f"Response {response}")
            return HttpResponse(json.dumps(response), status=401)
