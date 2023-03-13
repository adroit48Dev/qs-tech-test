from flask import Blueprint


currency_bp = Blueprint('api', __name__)

from . import routes
