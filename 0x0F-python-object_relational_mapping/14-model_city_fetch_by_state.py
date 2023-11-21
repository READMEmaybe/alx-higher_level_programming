#!/usr/bin/python3
"""
lists all City objects Grouped by State Objects
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    _ = session.query(State, City).join(City, State.id == City.state_id).all()
    for state, city in _:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
