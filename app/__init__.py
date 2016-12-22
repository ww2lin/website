from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db.db_config import SQLALCHEMY_DATABASE_URI

app_webSite = Flask(__name__)
app_webSite.config['DEBUG'] = True

app_webSite.config['SECRET_KEY'] = 'super-secret'

#account creation
app_webSite.config['SECURITY_REGISTERABLE'] = True
app_webSite.config['SECURITY_CONFIRMABLE'] = True
app_webSite.config['SECURITY_SEND_REGISTER_EMAIL'] = False
#password hash
app_webSite.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'
app_webSite.config['SECURITY_PASSWORD_SALT'] = 'this is some random salt :)'

#db
app_webSite.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# DB configuration.
db = SQLAlchemy(app_webSite)


