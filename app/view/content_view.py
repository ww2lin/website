from app import ww2lin_webSite
from flask import render_template
from dbmodels.models import *

@ww2lin_webSite.route('/')
def index():
    tuples = db.session.query(User, Blog).join(Blog).order_by('blog.id desc').limit(5)
    return render_template('index.html', tuples=tuples)

@ww2lin_webSite.route('/about')
@ww2lin_webSite.route('/about/<int:id>')
def about(id=1):
    return render_template('about.html')

@ww2lin_webSite.route('/blog/<int:id>')
def blog(id=1):
    blog = Blog.query.get(id)
    user = User.query.get(blog.user_id)
    return render_template('blog.html', user=user, blog=blog)

@ww2lin_webSite.route('/contact')
def contact():
    return render_template("contact.html")

