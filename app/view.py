from app import app

from flask import render_template

def view_index():
    # return 'HELLO'
    # def index():
    # print(view_index())
    # return view_index()
    return render_template('index.html', title='Index page')
