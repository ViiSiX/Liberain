"""
Docstring for liberain.API module.

This module contains functions which will be called
whenever the application receive the right API call.
"""

from ..liberain import app, api as _api, db, mail
from .. import constants
from flask_restful import Resource, \
    reqparse, \
    abort
from .. import utils


class ResourceGetNotAllowed(Resource):
    def get(self):
        abort(403, message=constants.ERROR_MESSAGES['GET_NOT_ALLOWED'])
