# -*- coding: utf-8 -*-
"""
Liberain
--------

A group focused social network used to store memories. This is
the API backend written on Flask framework.

:copyright: (c) 2017 by ViiSiX Team.
:license: MIT, see LICENSE for more details.
"""

from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


# creating Liberain using Flask.
app = Flask('liberain')
app.config.update({
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
})
app.config.from_object(__name__)
app.config.from_envvar('LIBERAIN_CONFIG')

# Register blueprint for API path and create API object.
api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)
app.register_blueprint(api_blueprint, url_prefix="/api/v1")

# Register DB object via SQLAlchemy.
db = SQLAlchemy(app)

# Register Mail object.
mail = Mail(app)
