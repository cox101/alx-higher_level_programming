#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    try:
        """Connect to MySQL server"""
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = db.cursor()

        """ Execute SQL query to retrieve states """
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        """ Display results"""
        for state in states:
            print(state)

        """ Close the database connection"""
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

