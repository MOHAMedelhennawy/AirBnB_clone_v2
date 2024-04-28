#!/usr/bin/python3
"""
City class, a subclass of BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.state import State

class City(BaseModel, Base):
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
