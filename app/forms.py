from wtforms import Form, StringField, TextAreaField, PasswordField

class RegisterForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')
    secret_key = StringField('Secret key')