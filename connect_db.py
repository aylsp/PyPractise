# coding=utf-8
import pymysql

config = {'host': 'localhost', 'port': 3306, 'user': 'root', 'passwd': 'canon', 'db': 'pingtest'}

def connect():
    connection = pymysql.connect(**config)
    return connection

def excute_sql(connection, sql):
    cur = connection.cursor()
    cur.execute(sql)
    connectiondb.commit()
    cur.close()
    connectiondb.close()

if __name__ == '__main__':
    sql = "delete FROM student_result where id%3=0;"
    connectiondb = connect()
    excute_sql(connectiondb, sql)
