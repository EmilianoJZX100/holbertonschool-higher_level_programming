#!/usr/bin/python3
"""takes in an argument and displays all values in the states table"""
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

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE '{}' \
        ORDER BY states.id".format(argv[4]))
    result = c.fetchall()

    for row in result:
        if row[1] == argv[4]:
            print(row)
