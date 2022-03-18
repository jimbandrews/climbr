import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from .models import db, UserModel

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

        new_user = UserModel(username, email, password)

        try:
            db.session.add(new_user)
            db.session.commit()
        except db.IntegrityError:
            error = f"Username {username} is already registered."
        else:
            return redirect(url_for("auth.login"))
        
        flash(error)

    return render_template('auth/register.html')
