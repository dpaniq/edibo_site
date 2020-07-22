# Bluerint it is an isolate application

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from flask_security import login_required
from flask_security import current_user

from models import Post, Tag, User
from .forms import PostForm

from app import db

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['post_title']
        body = request.form['post_body']
        user_id = int(request.form['user_id'])
        try:
            post = Post(title=title, body=body, author_id=user_id)
            db.session.add(post)
            db.session.commit()
        except:
            print('Something wrong with "Create Post!')
        return redirect(url_for('posts.index'))
    
    form = PostForm()
    title = 'Create Post'
    return render_template('posts/create_post.html', form=form, title=title)

@posts.route('/')
def index():
    
    q = request.args.get('q')
    page = request.args.get('page')  # ?page=<number>
    
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))  # becouse baseQuery .all()
    else:
        posts = Post.query.order_by(Post.created.desc())   
    
    for post in posts:
        post.body = post.body[0:100] + '...' if len(post.body) > 100 else post.body
    
    pages = posts.paginate(page=page, per_page=5)  # obj pagination
    return render_template('posts/index.html', posts=posts, pages=pages)


@posts.route('<slug>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first()
    
    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()
        
        return redirect(url_for('posts.post_detail', slug=post.slug))
    
    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)
        
        
@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    print('**** post ****\n', post)
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)