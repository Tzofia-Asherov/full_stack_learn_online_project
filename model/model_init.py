import pymysql
from config import DB_PASSWORD, DB_USER,DB_NAME


def connect_to_DB():
    connection = pymysql.connect(
        host="localhost",
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


# def connect_to_DB():
#     con = pymysql.connect(host = 'localhost',
#                       user = 'root',
#                       passwd =  '',
#                       db = 'learnonlinedb')
    
#     return con