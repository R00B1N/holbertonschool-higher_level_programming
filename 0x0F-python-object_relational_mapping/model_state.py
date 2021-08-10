#!/usr/bin/python3
"""
this module contains the class definition of a State
and an instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ the State class will be mapped to the mysql table states """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
