# from app import app
# from flask import render_template, flash, redirect, url_for

# from flask_login import current_user, login_user
# from app.models import User

# from app.forms import LoginForm
# from view import view_index

# @app.route('/')
# def index():
#     x = 'asd'
#     return 'asd'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     print("\n", dir(current_user), "\n")
#     if current_user.is_authenticted():
#         return redirect(url_for('index'))
#     form = LoginForm()

#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()

#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))

#         login_user(user, remember=form.remember_me.data)    
#         return redirect(url_for('index'))
#     return render_template('login.html', title='Sign in', form=form)

# https://pynative.com/python-generate-random-string/