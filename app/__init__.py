from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db.db_config import SQLALCHEMY_DATABASE_URI

ww2lin_webSite = Flask(__name__)
ww2lin_webSite.config['DEBUG'] = True

ww2lin_webSite.config['SECRET_KEY'] = 'super-secret'

#account creation
ww2lin_webSite.config['SECURITY_REGISTERABLE'] = True
ww2lin_webSite.config['SECURITY_CONFIRMABLE'] = True
ww2lin_webSite.config['SECURITY_SEND_REGISTER_EMAIL'] = False
#password hash
ww2lin_webSite.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'
ww2lin_webSite.config['SECURITY_PASSWORD_SALT'] = 'this is some random salt :)'

#db
ww2lin_webSite.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# DB configuration.
db = SQLAlchemy(ww2lin_webSite)


