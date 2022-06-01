from flask import Blueprint

bp_books = Blueprint('bp_books', __name__, cli_group='books')

from myapp.bp_books import views_books
from myapp.bp_books import modal_books
