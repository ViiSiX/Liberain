"""
    Docstring for liberain.views module.
    
    This module contains functions which will be called
    whenever the application receive the right url request.
"""

from flask import render_template
from .Liberain import app


@app.route('/')
def index():
    """Render and return About Page."""

    return render_template(
        "index.html"
    )
