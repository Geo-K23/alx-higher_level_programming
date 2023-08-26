#!/usr/bin/python3
"""
This script is an update to model_city.py and model_state.py
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """This is a representation of a city"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
