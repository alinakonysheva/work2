from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_compress import Compress
from flask_login import LoginManager

db = SQLAlchemy()

compress = Compress()

login_manager = LoginManager()


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_object('configuration.BaseConfiguration')

    db.init_app(app)

    compress.init_app(app)

    login_manager.init_app(app)
    login_manager.session_protection = "basic"
    login_manager.login_view = 'do_login'

    do_register_blueprint(app)

    do_register_error_handlers(app)
    with app.app_context():
        db.create_all()

    do_register_cli(app)

    if app.config['DEBUG']:
        app.debug = True
        toolbar = DebugToolbarExtension()
        toolbar.init_app(app)
    return app


def do_register_blueprint(flaskapp):
    from myapp.bp_general import bp_general
    from myapp.bp_users import bp_users
    from myapp.bp_books import bp_books

    flaskapp.register_blueprint(bp_general)
    flaskapp.register_blueprint(bp_users)
    flaskapp.register_blueprint(bp_books)


def do_register_error_handlers(flaskapp):
    from myapp.bp_general.views_general import do_not_authorized, do_not_found, do_server_error

    flaskapp.register_error_handler(404, do_not_found)
    flaskapp.register_error_handler(403, do_not_authorized)
    flaskapp.register_error_handler(406, do_not_authorized)
    flaskapp.register_error_handler(500, do_server_error)


def do_register_cli(flaskapp):
    from myapp.bp_general.utils_general import do_create_db
    from myapp.bp_users.cli_users import do_create_user, do_test_user_pass, \
        do_change_pass
    flaskapp.cli.add_command(do_create_db)
    flaskapp.cli.add_command(do_create_user)
    flaskapp.cli.add_command(do_test_user_pass)
    flaskapp.cli.add_command(do_change_pass)
