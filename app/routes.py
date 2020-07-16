

from app import app
# from flask import render_template

from view import view_index

@app.route('/')
def index():
    return view_index()
