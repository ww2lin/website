from app import ww2lin_webSite
from flask import render_template , request
from dbmodels.models import *

BLOG_PAGE_LIMIT = 3

@ww2lin_webSite.route('/')
def index():

    # user = User.query.get(1)
    offset = request.args.get("offset", 1, int)
    limit = request.args.get("limit", BLOG_PAGE_LIMIT, int)

    tuples = db.session.query(User, Blog).join(Blog).order_by(Blog.id.desc()).offset(offset).limit(limit)


    # Try to get offset-1 and limit + 1 pages, to determine if previous/next page is available for pagination
    hasOlderBlog = True if Blog.query.order_by(Blog.id.desc()).offset(offset+limit).first() else False
    hasNewerBlog = offset > 1 and tuples.count() > 0

    print Blog.query.order_by(Blog.id.desc()).offset(offset+limit).first()

    return render_template('index.html', tuples=tuples,
                           offset=offset,
                           limit=limit,
                           hasOlderBlog=hasOlderBlog,
                           hasNewerBlog=hasNewerBlog)


    # record_query = Blog.query.paginate(offset, limit, False).join(User)
    # total = record_query.total
    # record_items = record_query.items
    #
    # nextPage = offset + limit
    # return render_template('index.html', tuples=record_items, user=user)


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

