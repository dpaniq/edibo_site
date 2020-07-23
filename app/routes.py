

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
from app import user_datastore

from functions import random_secret_key


# @app.route('/')
# def index():
#     return view_index()

@app.route('/')
def index():
    return redirect('/posts')

# @app.route('/register', methods=['GET'])
# def register():
#     print('pff')
#     return render_template('security/register_user.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('sdasdadsasd!')
    return render_template('login.html', title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
        # return redirect(url_for('index'))
    if request.method == "POST":
        password = request.form['password']
        secret_key = request.form['secret_key']
        email = request.form['email']
        fullname = request.form['first_name'] + ' ' + request.form['last_name']
        
        secret = SecretKey.query.filter(SecretKey.secret_key == secret_key).first()
        if secret and secret.expired == False:
            secret.expired = True
            try:
                # user = User(fullname=fullname, email=email, password=password, active=True)
                # db.session.add(user)
                # flask-security
                user_datastore.create_user(fullname=fullname, email=email, password=password)
                db.session.commit()
                return redirect('/login')
            except Exception as e:
                print(e, '\nSomething wrong with "Register"!\n')
        else: 
            flash(f'Secret key "{secret_key}" has been expired')
            flash('...call to +371 29952-Zzz-zZz-zz.... :]')           
    form = RegisterForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/admin/secret_key', methods=['GET', 'POST'])
@login_required
def secret_key():
    
    # print('ROLE', current_user.has_role('admin'), current_user.roles)
    
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
    