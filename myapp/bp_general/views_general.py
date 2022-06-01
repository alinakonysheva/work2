from flask import render_template, abort, redirect, flash, url_for, current_app
from myapp import db
from myapp.bp_general import bp_general
from flask_login import current_user
from myapp.bp_books.controller_books import ControllerBook
from myapp.bp_books.form_books import SearchForm
from myapp.bp_users.model_users import load_user
@bp_general.route('/')
def do_home():
    if current_user and current_user.is_authenticated:
        user_id = current_user.get_id()
        user = load_user(user_id)
        controller = ControllerBook(db.session)
        return render_template('books/home.html', ids=controller.get_all_ids(), form=SearchForm(), user=user)
    else:
        return render_template('general/home.html')


def do_not_found(error):
    return render_template('general/errors.html', code=404, error=error)


def do_not_authorized(error):
    return render_template('general/errors.html', code=403, error=error)


def do_server_error(error):
    return render_template('general/errors.html', code=500, error=error)