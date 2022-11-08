#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
#create connection
db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], password=argv[2], database=argv[3])

mycursor= db.cursor()
query = "SELECT * FROM states ORDER BY states.id ASC"
mycursor.execute(query)
result = mycursor.fetchall()
print(result)

for record in result:
    print(record)