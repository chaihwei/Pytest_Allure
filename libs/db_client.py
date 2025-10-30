import pymysql
from pymysql.cursors import DictCursor
from contextlib import contextmanager

class MysqlClient:
    def __init__(self, host, port, user, password, database, charset="utf8mb4"):
        self.config = {
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "database": database,
            "charset": charset,
            "cursorclass": DictCursor
        }

    @contextmanager
    def connect(self):
        conn = pymysql.connect(**self.config)
        cursor = conn.cursor()
        try:
            yield conn, cursor
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def query(self, sql, params=None):
        with self.connect() as (conn, cursor):
            cursor.execute(sql, params)
            return cursor.fetchall()
        
    def execute(self, sql, params=None):
        with self.connect() as (conn, cursor):
            return cursor.execute(sql, params)