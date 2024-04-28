#!/usr/bin/python3
"""
City class, a subclass of BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    """
    A subclass of BaseModel class
    Public class attributes:
        state_id: (str) will be State.id
        name:     (str)
    """
    # state_id = ""
    # name = ""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
