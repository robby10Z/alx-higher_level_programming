#!/usr/bin/python3
"""
script that takes in the name of a
state as an argument and lists all cities of that state
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
    sql = """SELECT cities.name
            FROM cities
            JOIN states
            ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id"""
    cursor.execute(sql, (argv[4], ))
    results = cursor.fetchall()
    if results == ():
        print("")
    else:
        for i in range(len(results)):
            if i == len(results)-1:
                print(results[i][0])
            else:
                print("{}, ".format(results[i][0]), end="")
    cursor.close()
    db.close()
