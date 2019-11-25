from flask import Blueprint

bp = Blueprint('main',__name__)

from flaskproject.main import routes
