from flask import Flask
from config import Configuration

from posts.blueprint import posts

app = Flask(__name__) # name current file
app.config.from_object(Configuration)

app.register_blueprint(posts, url_prefix='/blog')