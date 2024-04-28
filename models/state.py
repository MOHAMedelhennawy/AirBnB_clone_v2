#!/usr/bin/python3
"""
State class, a subclass of BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel, Base):
    """
    A subclass of BaseModel class

    Public class attribute:
    name (str): state name
    """

    # name = ""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
