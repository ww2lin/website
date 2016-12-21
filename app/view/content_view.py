from app import ww2lin_webSite, db
from flask import render_template
from dbmodels.models import User

@ww2lin_webSite.route('/')
@ww2lin_webSite.route('/blog')
def index():
    return render_template('blog.html')

@ww2lin_webSite.route('/about')
def about():
    return render_template('about.html')

