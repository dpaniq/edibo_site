

from app import app
# from flask import render_template

from view import view_index

from flask import render_template
from flask import redirect
from flask import request
from flask import url_for


from flask_login import current_user, login_user
from models import User

from forms import RegisterForm
from app import db
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
        print(request.form)
        
        username = request.form['username']
        password = request.form['password']
        secret_key = request.form['secret_key']
        
        # if secret_key
        
        try:
            user = User(email=username, password=password)
            db.session.add(user)
            db.session.commit()
            
            print('user dobavlen')
            
            return redirect('/login')
            
            
        except Exception as e:
            print(e)
            print('Something wrong with create post!')
    

    form = RegisterForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user is None or not user.check_password(form.password.data):
    #         flash('Invalid username or password')
    #         return redirect(url_for('login'))
    #     login_user(user, remember=form.remember_me.data)
    #     return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)