#!/usr/bin/python3
"""
Script that prints the `State` object in `hbtn_0e_0_usa`
where `name` matches the argument `state name to search`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name to search (str)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_state_by_name(username, password, database, state_name):
    try:
        # Create engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Create session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query state by name
        state = session.query(State).filter(State.name == state_name).first()

        # Print state id if found, otherwise print "Not found"
        if state:
            print(state.id)
        else:
            print("Not found")

        # Close session
        session.close()

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    print_state_by_name(username, password, database, state_name)

