#!/usr/bin/python3
"""
State class, a subclass of BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine import file_storage


class State(BaseModel, Base):
    """
    A subclass of BaseModel class

    Public class attribute:
    name (str): state name
    """

    # name = ""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        all_cities = file_storage.FileStorage.all(self)
        return all_cities
