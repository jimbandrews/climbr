import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from .models import db, User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        error = None

        if not username:
            error = "Username is required."
        elif not email:
            error = "Email is required."
        elif not password:
            error = "Password is required."

        new_user = User(username, email, generate_password_hash(password))

        try:
            db.session.add(new_user)
            db.session.commit()
        except db.IntegrityError:
            error = f"Username {username} is already registered."
        else:
            return redirect(url_for("auth.login"))
        
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        error = None

        if user is None:
            error = "Incorrect Username."
        elif not check_password_hash(user.password, password):
            error = "Incorrect Password"

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('auth.index'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    return redirect(url_for('auth.index'))


@bp.route('/index', methods=('GET',))
def index():
    return render_template('climbr/test.html')