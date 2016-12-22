from flask import render_template, request, jsonify, redirect
from dbmodels.models import *
from flask_security import login_required, current_user, user_registered
from temp.models import *

BLOG_PAGE_LIMIT = 3

@app_webSite.route('/')
@app_webSite.route('/<message>')
def index(message=None):
    # handle new blog submissions
    if message == 'success':
        message = Message("success", "Success!", "You blog has been submitted.")
    elif message == 'fail':
        message = Message("warning", "Warning!", "You blog is not submitted due to missing title/content")
    else:
        message = None

    offset = request.args.get("offset", 0, int)
    tuples = db.session.query(User, Blog).join(Blog).order_by(Blog.id.desc()).offset(offset).limit(BLOG_PAGE_LIMIT)

    # Try to get offset-1 and limit + 1 pages, to determine if previous/next page is available for pagination
    hasOlderBlog = True if Blog.query.order_by(Blog.id.desc()).offset(offset+BLOG_PAGE_LIMIT).first() else False
    hasNewerBlog = offset > 1 and tuples.count() > 0

    return render_template('bloglistwrapper.html', tuples=tuples,
                           offset=offset,
                           limit=BLOG_PAGE_LIMIT,
                           hasOlderBlog=hasOlderBlog,
                           hasNewerBlog=hasNewerBlog,
                           message=message)

@app_webSite.route('/about')
@app_webSite.route('/about/<int:id>')
def about():
    return render_template('about.html')

@app_webSite.route('/blog/<int:id>')
def blog(id=1):
    blog = Blog.query.get(id)
    user = User.query.get(blog.user_id)
    return render_template('blogdetails.html', user=user, blog=blog)

@app_webSite.route('/contact')
def contact():
    return render_template("contact.html")

@app_webSite.route('/postblog')
@login_required
def postblog():
    return render_template("postblog.html")

@app_webSite.route('/submitblog', methods=['POST'])
@login_required
def submitblog():
    title = request.form["title"]
    header = request.form["header"]
    content = request.form["content"]
    result = 'fail'
    if title is not None and content is not None:
        newblog = Blog(title, content, current_user.id, header)
        db.session.add(newblog)
        db.session.commit()
        result = 'success'
    return redirect('/'+result)

@app_webSite.route('/moreblog', methods=['POST'])
def moreblog():
    offset = request.form['offset']
    tuples = None
    if offset.isdigit():
        offset = int(offset)
        tuples = db.session.query(User, Blog).join(Blog).order_by(Blog.id.desc()).offset(offset).limit(BLOG_PAGE_LIMIT)

        if not Blog.query.order_by(Blog.id.desc()).offset(int(offset)+BLOG_PAGE_LIMIT).first():
            offset = -1
        else:
            offset += BLOG_PAGE_LIMIT
    else:
        offset = -1
    return jsonify({"nextOffset": offset, "limit" : BLOG_PAGE_LIMIT, "bloghtml": render_template("bloglist.html", tuples=tuples)})

#register
@user_registered.connect_via(app_webSite)
def user_registered_sighandler(app_webSite, user, confirm_token):
    role = user_datastore.find_or_create_role(USER)
    user_datastore.add_role_to_user(user, role)
    db.session.commit()

#error routes
@app_webSite.errorhandler(404)
def page_not_found(error):
    return render_template('/error/404.html'), 404

@app_webSite.errorhandler(500)
def internal_server_error(error):
    return render_template('/error/500.html'), 500