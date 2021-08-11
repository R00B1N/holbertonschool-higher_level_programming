#!/usr/bin/python3
""" a script that lists all City objects from the database hbtn_0e_14_usa """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def main(argv):
    """ main function """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance, st in session.query(City, State)\
            .filter(City.state_id == State.id).order_by(asc(City.id)):
        print("{}: ({}) {}".format(st.name, instance.id, instance.name))
    session.close()


if __name__ == '__main__' and len(sys.argv) == 4:
    main(sys.argv)
