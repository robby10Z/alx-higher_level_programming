#!/usr/bin/python3
"""
script that lists all State objects from the
database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import model_state
from model_state import Base
import sys
if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    mySession = Session()
    for st_obj in mySession.query(model_state.State).\
            order_by(model_state.State.id).all():
        print("{}: {}".format(st_obj.id, st_obj.name))

    mySession.close()
