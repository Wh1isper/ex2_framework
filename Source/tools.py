import mysql.connector as connector
import json


def connect_to_mysql():
    with open("config.json") as f:
        config = json.load(f)
    conn = connector.connect(**config)
    return conn


def quary(statement, fetch_num=0):
    print(statement)
    with connect_to_mysql() as conn:
        cursor = conn.cursor()
        cursor.execute(statement)
        if fetch_num:
            res = cursor.fetchmany(fetch_num)
        else:
            res = cursor.fetchall()
    return res


def connection_test():
    global conn
    print("测试数据库连接...")
    try:
        conn = connect_to_mysql()
        print("数据库连接成功！")
        conn.close()
    except:
        print("数据库连接失败，检查config.json")
        exit(-1)

connection_test()