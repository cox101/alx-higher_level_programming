#!/usr/bin/python3
"""
Script that lists all `City` objects from the database `hbtn_0e_101_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_all_cities(username, password, database):
    try:
        # Create engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Create session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query all cities
        cities = session.query(City)

        # Print city details
        for city in cities:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))

        # Close session
        session.close()

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_all_cities(username, password, database)

