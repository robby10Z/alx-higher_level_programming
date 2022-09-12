#!/usr/bin/python3
"""
Write a script that takes in an argument and displays
all values in the states table of
hbtn_0e_0_usa where name matches the argument.
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
    cursor.execute(
        "SELECT * FROM states WHERE Name LIKE BINARY '{}' ORDER BY id ASC"
        .format(argv[4]))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
