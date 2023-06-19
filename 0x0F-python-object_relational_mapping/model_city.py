#!/usr/bin/python3
'''
class definition for city
'''
from sqlalchemy import Column, String, Foreignkey
from sqlalchemy.ext.declarative import declarative_base


Base = declarataive_base()


class City(Base):
    '''
    City class inherits from base
    '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey('state.id'), nullable=False)
