

from app import app
# from flask import render_template

from view import view_index

from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import abort
from flask import flash

from flask_security import login_required
from flask_login import current_user, login_user
from models import User, SecretKey

from forms import RegisterForm
from app import db

from functions import random_secret_key


@app.route('/')
def index():
    return view_index()

# @app.route('/register', methods=['GET'])
# def register():
#     print('pff')
#     return render_template('security/register_user.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
        # return redirect(url_for('index'))
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        secret_key = request.form['secret_key']
        
        secret = SecretKey.query.filter(SecretKey.secret_key == secret_key).first()
        if secret and secret.expired == False:
            secret.expired = True
            try:
                user = User(email=username, password=password, active=True)
                db.session.add(user)
                db.session.commit()
                return redirect('/login')
            except Exception as e:
                print(e, '\nSomething wrong with "Register"!\n')
        else: 
            flash(f'Secret key "{secret.secret_key}" has been expired')            
    form = RegisterForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user is None or not user.check_password(form.password.data):
    #         flash('Invalid username or password')
    #         return redirect(url_for('login'))
    #     login_user(user, remember=form.remember_me.data)
    #     return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/admin/secret_key', methods=['GET', 'POST'])
@login_required
def secret_key():
    print(dir(current_user))
    
    print('ROLE', current_user.has_role('admin'), current_user.roles)
    
    if not current_user.has_role('admin'):
        return abort(404, description="Resource not found... Becouse your are not admin :)")
        
    
    if request.method == 'POST':
        secret_key = request.form['secret_key']
        try:
            secret = SecretKey(secret_key=secret_key, expired=False)
            db.session.add(secret)
            db.session.commit()
            return redirect(url_for('secret_key'))
        except Exception as e:
            print(e, '\nSomething wrong with "Secret key"!\n')
    
    secret_key = random_secret_key()
    secret_key_list = SecretKey.query.all()        
        
    return render_template('admin/secret_key.html', secret_key=secret_key, secret_key_list=secret_key_list)
    