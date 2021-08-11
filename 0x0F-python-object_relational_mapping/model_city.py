#!/usr/bin/python3
"""
this module contains the class definition of cities table, 'City'
and an instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """ the City class will be mapped to the mysql table cities """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
