#!/usr/bin/python3
"""
This is similar to model_state.py named model_city.py but contains the class
definition of a City.
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Representation of a city"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))