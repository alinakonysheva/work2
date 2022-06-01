import click
from flask.cli import with_appcontext
from myapp import db
from myapp.bp_users.model_users import User
from myapp.bp_users import bp_users


@bp_users.cli.command("create-user")
@click.argument('email')
@click.argument('username')
@click.argument('password')
@with_appcontext
def do_create_user(email, username, password):
    user = User()
    user.email = email
    user.username = username
    user.set_password(password)
    db.session.add(user)
    db.session.commit()


@bp_users.cli.command("test-user-pass")
@click.argument('id')
@click.argument('password')
@with_appcontext
def do_test_user_pass(id, password):
    user = User.query.get(id)
    if user:
        print('veryfing pass for user: "{}" with email: "{}"'.format(user.username, user.email))
        if user.check_password(password):
            print('user password is valid')
            return

    print('user password is not correct')


@bp_users.cli.command("change-pass")
@click.argument('id')
@click.argument('password')
@with_appcontext
def do_change_pass(id, password):
    user = User.query.get(id)
    if user:
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
