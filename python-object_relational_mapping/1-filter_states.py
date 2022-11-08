#!/usr/bin/python3
"""lists all states with a name starting with N from the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
        )

    cu = db.cursor()
    cu.execute("SELECT * FROM states WHERE name = 'N%' ORDER BY states.id ASC")
    result = cu.fetchall()

    for row in result:
        print(row)
