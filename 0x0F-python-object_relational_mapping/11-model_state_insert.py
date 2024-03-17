#!/usr/bin/python3
"""
Script that adds the `State` object “Louisiana”
to the database `hbtn_0e_6_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(username, password, database):
    try:
        # Create engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Create session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Add new state
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        # Print the id of the new state
        print(new_state.id)

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

    add_state(username, password, database)

