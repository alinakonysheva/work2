from flask import Blueprint

bp_users = Blueprint('bp_users', __name__, cli_group="user")

from . import views_users
from . import model_users
