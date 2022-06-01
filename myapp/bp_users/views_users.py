import logging
from flask import render_template, abort, flash, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from myapp import db
from myapp.bp_users import bp_users
from myapp.bp_users.model_users import User, only_admins
from myapp.bp_users.form_users import ProfileForm, LoginForm, SignUpForm
from myapp.bp_general.consts import MESSAGES_ERROR, MESSAGES_OK, MESSAGES_WARNING


@bp_users.route('/myprofile', methods=['GET', 'POST'])
@login_required
def do_my_profile():
    form = ProfileForm()

    user = User.query.get(1)
    if user:
        if form.validate_on_submit():
            user.username = form.username.data
            user.email = form.email.data
            db.session.add(user)
            db.session.commit()

        form.username.data = user.username
        form.email.data = user.email

        return render_template('users/myprofile.html', form=form, user=user)

    abort(404)


@bp_users.route('/user', defaults={'user_id': 0}, methods=['GET', 'POST'])
@bp_users.route('/user/<int:user_id>', methods=['GET', 'POST'])
@login_required
@only_admins
def do_user(user_id):
    form = ProfileForm()
    if user_id == 0:
        user = User()
    else:
        user = db.session.query(User).get(user_id)
        if user is None:
            flash('gebruiker bestaat niet')

    if user:
        if form.validate_on_submit():
            user.username = form.username.data
            user.email = form.email.data
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('bp_users.do_user', user_id=user.id))

        form.username.data = user.username
        form.email.data = user.email

        return render_template('users/myprofile.html', form=form, user=user)

    abort(404)


@bp_users.route('/sign-up', methods=['GET', 'POST'])
def do_signup():
    user = current_user
    if user and user.is_authenticated:
        flash('You are already logged in, you can not signup', MESSAGES_WARNING)
        return redirect(url_for('bp_general.do_home'))

    form = SignUpForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.set_password(form.password.data)
        user.profile_type = 1

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('bp_users.do_login', user_id=user.id))

    return render_template('users/signup.html', form=form)


@bp_users.route('/users')
@login_required
@only_admins
def do_users():
    users = db.session.query(User).all()
    return render_template('users/userlist.html', users=users)


@bp_users.route("/login", methods=["GET", "POST"])
def do_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if not user.check_password(form.password.data):
                flash('Wrong password', MESSAGES_WARNING)
            else:
                # in case we have another user still logged in
                if current_user and current_user.is_authenticated:
                    try:
                        current_user.authenticated = False
                        db.session.add(current_user)
                        db.session.commit()
                        logout_user()
                    except Exception as e:  # pragma: no cover
                        # if this fails we do not care, but we certainly do not want to block 
                        # someone logging in 
                        logging.info('Error during login (logout): {}'.format(e))

                # now set the new user to authenticated
                user.authenticated = True
                db.session.add(user)
                db.session.commit()

                # do the actual login
                login_user(user, remember=form.remember_me.data)

                flash('You are now logged in', MESSAGES_OK)

                return redirect(url_for('bp_general.do_home'))
        else:
            flash('Wrong password', MESSAGES_ERROR)

    return render_template('users/login.html', form=form)


@bp_users.route("/logout", methods=["GET"])
@login_required
def do_logout():
    user = current_user
    if user and user.is_authenticated:
        user.authenticated = False
        db.session.add(user)
        db.session.commit()
        flash('You are now logged out')
        logout_user()
        return redirect(url_for('bp_general.do_home'))

