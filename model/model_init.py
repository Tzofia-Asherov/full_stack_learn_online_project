import pymysql
from config import DB_PASSWORD, DB_USER


def connect_to_DB():
    connection = pymysql.connect(
        host="localhost",
        user=DB_USER,
        password=DB_PASSWORD,
        db="pokemon",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
