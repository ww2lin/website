from dbmodels.models import *
from flask_security import SQLAlchemyUserDatastore, Security
from app import ww2lin_webSite
# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(ww2lin_webSite, user_datastore)

