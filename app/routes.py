from app import app
from flask import render_template, flash, redirect, url_for

from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Mock"}
    return render_template('index.jinja', title='Index page', user=user)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))

    else:
        print('trololo')
    return render_template('login.jinja', title='Sign In', form=form)

# https://pynative.com/python-generate-random-string/