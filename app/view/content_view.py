from app import ww2lin_webSite
from flask import render_template, request
from dbmodels.models import *
from flask import jsonify


BLOG_PAGE_LIMIT = 3

@ww2lin_webSite.route('/')
def index():

    offset = request.args.get("offset", 1, int)

    tuples = db.session.query(User, Blog).join(Blog).order_by(Blog.id.desc()).offset(offset).limit(BLOG_PAGE_LIMIT)


    # Try to get offset-1 and limit + 1 pages, to determine if previous/next page is available for pagination
    hasOlderBlog = True if Blog.query.order_by(Blog.id.desc()).offset(offset+BLOG_PAGE_LIMIT).first() else False
    hasNewerBlog = offset > 1 and tuples.count() > 0

    return render_template('bloglistwrapper.html', tuples=tuples,
                           offset=offset,
                           limit=BLOG_PAGE_LIMIT,
                           hasOlderBlog=hasOlderBlog,
                           hasNewerBlog=hasNewerBlog)

@ww2lin_webSite.route('/about')
@ww2lin_webSite.route('/about/<int:id>')
def about(id=1):
    return render_template('about.html')

@ww2lin_webSite.route('/blog/<int:id>')
def blog(id=1):
    blog = Blog.query.get(id)
    user = User.query.get(blog.user_id)
    return render_template('blogdetails.html', user=user, blog=blog)

@ww2lin_webSite.route('/contact')
def contact():
    return render_template("contact.html")

@ww2lin_webSite.route('/moreblog', methods=['POST'])
def moreblog():

    offset = request.form['offset']
    tuples = None
    if offset.isdigit():
        offset = int(offset)
        tuples = db.session.query(User, Blog).join(Blog).order_by(Blog.id.desc()).offset(offset).limit(BLOG_PAGE_LIMIT)

        if not Blog.query.order_by(Blog.id.desc()).offset(int(offset)+BLOG_PAGE_LIMIT).first():
            offset = -1
        else:
            offset = offset + BLOG_PAGE_LIMIT
    else:
        offset = -1;
    print offset
    return jsonify({"nextOffset": offset, "limit" : BLOG_PAGE_LIMIT, "bloghtml": render_template("bloglist.html", tuples=tuples)})


