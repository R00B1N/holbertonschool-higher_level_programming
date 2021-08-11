#!/usr/bin/python3
""" this script updates an objectin the table 'states'
in the database hbtn_0e_6_usa
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
    instance = session.query(State).filter(State.id == 2).one()
    instance.name = "New Mexico"
    session.commit()
    session.close()


if __name__ == '__main__' and len(sys.argv) == 4:
    main(sys.argv)
