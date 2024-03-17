#!/usr/bin/python3
"""
Script that lists all values in the `states` table of `hbtn_0e_0_usa`
where `name` matches the argument `state name searched`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name searched (str)
"""

import sys
import MySQLdb

def list_states(username, password, database, state_name):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute query
        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id", (state_name,))

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
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_states(username, password, database, state_name)

