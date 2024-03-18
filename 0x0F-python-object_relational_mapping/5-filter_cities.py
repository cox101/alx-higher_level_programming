#!/usr/bin/python3
"""
Script that lists all `cities` in the `cities` table of `hbtn_0e_4_usa`
where the city's state matches the argument `state name`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name (str)
"""

import sys
import MySQLdb

def list_cities_by_state(username, password, database, state_name):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute query
        cursor.execute("SELECT c.name FROM cities c INNER JOIN states s ON c.state_id = s.id WHERE s.name = %s ORDER BY c.id", (state_name,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Print results
        for i in range(len(rows)):
            print(rows[i][0], end=", " if i + 1 < len(rows) else "")
        print("")

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close connection
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(username, password, database, state_name)

