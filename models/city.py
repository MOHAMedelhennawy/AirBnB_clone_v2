#!/usr/bin/python3
"""
City class, a subclass of BaseModel
"""
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(BaseModel, Base):
    """
    A subclass of BaseModel class
    Public class attributes:
        state_id: (str) will be State.id
        name:     (str)
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, state_id="", name=""):
        """
        City Model constructor
        """
        self.state_id = state_id
        self.name = name
