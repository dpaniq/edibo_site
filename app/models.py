import re
from app import db
from datetime import datetime


from flask_security import UserMixin, RoleMixin
# from app import login
# from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '_', s)

# many to many

post_tags = db.Table('posts_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # many to many (+ lazy -> BaseQuery Object : for additional methods)
    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'<Post {self.id} with {self.slug}>'

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return f'<Tag{self.id} with {self.name}>'



### Flask Security ###

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(120), unique=True)
    active = db.Column(db.Boolean())
    
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    author = db.relationship('Post', backref='author', lazy='dynamic')
        
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def __repr__(self):
    #     return '<User {}>'.format(self.username) 

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
    
    def __repr__(self):
        return f'{self.name}'


class SecretKey(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    secret_key = db.Column(db.String(20), unique=True)
    expired = db.Column(db.Boolean())
    
    def __repr__(self):
        return f'{self.secret_key} - [Expired]: {self.expired}'