from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField,\
    BooleanField


class ProfileForm(FlaskForm):
    username = StringField('Username', id='profile_username')
    email = EmailField('Email', id='profile_email')
    submit = SubmitField('Save', id='profile_submit')


class LoginForm(FlaskForm):
    email = StringField('Email', id='login_email')
    password = PasswordField('Password', id='login_password')
    remember_me = BooleanField('Keep me logged in', id='remember_me')
    submit = SubmitField('Log In', id='login_submit')


class SignUpForm(FlaskForm):
    email = StringField('Email', id='signup_email')
    username = StringField('Username', id='signup_username') 
    password = PasswordField('Password', id='signup_password')
    submit = SubmitField('Submit', id='signup_submit')
