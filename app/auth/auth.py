import time
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .. import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    print(email, password)

    user = User.query.filter_by(email=email).first()
    if user:  # if user found
        print('User found')
        flash('Email address already exists!')
        time.sleep(10)
        return redirect(url_for('auth.login'))
    else:
        new_user = User(email=email, name=name,
                        password=generate_password_hash('sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return 'Logout'
