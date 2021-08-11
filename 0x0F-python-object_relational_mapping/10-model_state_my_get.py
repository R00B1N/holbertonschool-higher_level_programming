#!/usr/bin/python3
""" a script that lists all State objects from the database hbtn_0e_6_usa
with the given name
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def main(argv):
    """ main function """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        instance = session.query(State).filter(State.name == argv[4]).one()
        print(str(instance.id))
    except:
        print("Not found")
    session.close()


if __name__ == '__main__' and len(sys.argv) == 5:
    main(sys.argv)
