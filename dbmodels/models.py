from app import db, app_webSite
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore, Security

# Define models
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    created = db.Column(db.TIMESTAMP, server_default=db.func.now())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    blog = db.relationship('Blog')

    def __repr__(self):
        return "<User %r>" % self.username

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    header = db.Column(db.String)
    created = db.Column(db.TIMESTAMP, server_default=db.func.now())
    last_updated = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.current_timestamp())
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, content, user_id, header=None):
        self.title = title
        self.header = header
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Blog id:%r title:%r>" % (self.id, self.title)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app_webSite, user_datastore)

def initData():
    user_datastore.create_role(name=ADMIN)
    user_datastore.create_role(name=USER)

#Roles
ADMIN = 'admin'
USER = 'user'