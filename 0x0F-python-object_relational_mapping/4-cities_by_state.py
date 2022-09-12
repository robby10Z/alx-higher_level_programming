#!/usr/bin/python3
"""
script cript that lists all cities from the database
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
    sql = ("SELECT cities.id, cities.name, states.name FROM cities" +
           " INNER JOIN states ON cities.state_id = states.id ORDER BY" +
           " cities.id ")
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
