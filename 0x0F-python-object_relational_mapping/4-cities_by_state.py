#!/usr/bin/python3
"""
Script that lists all `cities` from the database `hbtn_0e_4_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
import MySQLdb

def list_cities(username, password, database):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute query
        cursor.execute("SELECT c.id, c.name, s.name FROM cities c INNER JOIN states s ON c.state_id = s.id ORDER BY c.id")

        # Fetch all rows
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close connection
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)

