import logging

from django.http import JsonResponse
from elasticsearch.exceptions import ConnectionError
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """Custom exception handler for elasticsearch.exceptions.ConnectionError

    Args:
        exc (Exception): exception to be handled
        context (dict): context dict

    Returns:
        Response: returns processed exception request
    """
    response = exception_handler(exc, context)

    if isinstance(exc, ConnectionError):
        err_data = {"details": "Search service is not available now. Try again later."}

        logging.error(f"Original error detail and callstack: {exc}")
        return JsonResponse(err_data, status=503)

    return response
