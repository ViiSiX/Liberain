"""
Docstring for liberain.views module.

This module contains functions which will be called
whenever the application receive the right url request.
"""

import os
from flask import render_template, send_from_directory
from .liberain import app


@app.route('/')
def index():
    """Render and return About Page."""

    return render_template(
        "index.html"
    )


@app.route('/favicon.ico')
def favicon():
    """Return a favicon to browser."""

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')
