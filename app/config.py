import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):

    DEBUG = True

    SECRET_KEY = 'jh123hj123hj123hj21g3123712SADSAD123'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    ### Flask-security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    
    # SECURITY_REGISTERABLE = True
    # SECURITY_REGISTER_URL = '/register'