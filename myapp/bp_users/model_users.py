import logging
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from flask_login import UserMixin, current_user
from flask import abort
from myapp import db, login_manager


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True, index=True)
    email = db.Column('email', db.String(200), unique=True)
    username = db.Column('username', db.String(200))
    __password = db.Column('password', db.String(200))
    active = db.Column('active', db.Boolean)
    profile_type = db.Column('profile', db.Integer, default=1)
    wishlist = db.relationship('Wishlist', back_populates="user", uselist=False)

    # 0 - admin
    # 1 - user

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.__password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.__password, password)

    def is_admin(self):
        return self.profile_type == 0

    @property
    def is_author(self):
        try:
            return (self.profile_type == 0)
        except:
            return False


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
        # return user if user and (not user.is_banned or not user.is_active) else None
    except Exception as e:
        logging.error('error loading user {}: {}'.format(user_id, e))
    return None


def only_admins(func):
    @wraps(func)
    def is_allowed(*args, **kwargs):
        cu = current_user
        if cu is not None and cu.profile_type == 0:
            return func(*args, **kwargs)
        else:
            abort(403)

    return is_allowed