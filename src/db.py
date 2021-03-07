"""
Package: src.db
Filename: db.py
Author(s): Grant W
"""
# Python Imports
import os

# Third Party Imports
import sqlalchemy as sa
from sqlalchemy.sql import text

# Local Imports

conn_str = "mysql+mysqlconnector://{}:{}@{}/{}".format(
    os.environ['DB_USER'],
    os.environ['DB_PASS'],
    os.environ['DB_HOST'],
    os.environ['DB_NAME']
)

class DB:

    def __init__(self):
        self.db_engine = sa.create_engine(conn_str,
                                          pool_size=1,
                                          max_overflow=5,
                                          pool_recycle=3600)

    def get_last_insert_id(self, db_result):
        """Get the last insert id from a result object"""
        return db_result.context.cursor._last_insert_id

    def perform_insert(self, query, params={}):
        """Return the id of an inserted item"""
        res = self.execute_raw(query, params)
        return self.get_last_insert_id(res)

    def execute_raw(self, query, params={}):
        """returns raw response from query"""
        return self.db_engine.execute(query, params)

    def execute_query(self, query, params={}):
        """returns dict'd response from query"""
        res = self.execute_raw(query, params).fetchall()
        return [dict(x) for x in res]

    def select_one(self):
        return self.execute_query("SELECT 1000;")

db = DB()