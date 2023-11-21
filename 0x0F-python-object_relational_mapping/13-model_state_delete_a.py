#!/usr/bin/python3
"""
Update a State object where id = 2 to New Mexico
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    to_delete = session.query(State).filter(State.name.like("%a%")).all()
    if to_delete:
        for state in to_delete:
            session.delete(state)
    session.commit()
