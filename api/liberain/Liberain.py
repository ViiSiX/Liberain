# -*- coding: utf-8 -*-
"""
    Liberain
    --------
    
    A group focused social network used to store memories. This is
    the API backend written on Flask framework.
    
    :copyright: (c) 2017 by ViiSiX Team.
    :license: MIT, see LICENSE for more details.
"""

from flask import Flask


# creating Liberain using Flask
app = Flask('liberain')
app.config.from_object(__name__)
app.config.from_envvar('LIBERAIN_CONFIGS', silent=True)
