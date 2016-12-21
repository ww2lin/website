import sys

from app import db
from default_config import USER_LIST, BLOG_LIST
from dbmodels import models

class Populate(object):
    """Populate class which contains methods to pre-insert meta data to database.
    """
    @classmethod
    def user(cls):
        for user in USER_LIST:
            entry = models.User(**user)
            db.session.add(entry)

    @classmethod
    def blog(cls):
        for blog in BLOG_LIST:
            entry = models.Blog(**blog)
            db.session.add(entry)

class RebuildDB(object):

    @classmethod
    def _purgeTables(cls):
        """Delete entries from all tables in the database.
        """
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            print 'Clear table %s' % table
            db.session.execute(table.delete())
        db.session.commit()

    @classmethod
    def _populateTables(cls):
        """Insert entries with predefined data into the databse.
        """
        for method in dir(Populate):
            if not method.startswith('__'):
                populateTable = getattr(Populate, method)
                print 'Inserting data into %s table ...' % method
                populateTable()

        db.session.commit()


    @classmethod
    def initiate(cls):
        """Initiate a new database. It will purge all tables and build new ones.
        """
        cls._purgeTables()
        cls._populateTables()
        print 'DB initialization finished!'


def main():
    RebuildDB.initiate()
    return 0


if __name__ == '__main__':
    sys.exit(main())
