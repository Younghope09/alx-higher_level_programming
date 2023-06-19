#!/usr/bin/python3
'''
Prints the first state object with the name passed as an argumenrt from the databse hbtn_0e_6_usa
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3],\
pool_pre_ping=True))
    state_name = argv[4]
    flag = 0

    
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id)

    for i in first_state:
        if i.name == state_name:
            print('{}'.format(i.id))
            flag = 1
    if not flag:
        print('Not found')

    session.close()
