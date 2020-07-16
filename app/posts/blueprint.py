# Bluerint it is an isolate application

from flask import Blueprint
from flask import render_template

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
    return render_template('posts/index.jinja')