#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],
    )
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE Name LIKE BINARY 'N%' ORDER BY id "
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
    