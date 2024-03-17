#!/usr/bin/python3
"""
Script that creates the `State` “California” with the
`City` “San Francisco” from the database `hbtn_0e_100_usa`.

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


def create_state_and_city(username, password, database):
    try:
        # Create engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Create session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create state
        new_state = State(name="California")
        session.add(new_state)
        session.flush()  # Flush to get the state id

        # Create city associated with the state
        new_city = City(name="San Francisco", state_id=new_state.id)
        session.add(new_city)

        # Commit changes
        session.commit()

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

    create_state_and_city(username, password, database)

