#!/usr/bin/python3
"""
State class, a subclass of BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class State(BaseModel, Base):
    """
    A subclass of BaseModel class

    Public class attribute:
    name (str): state name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relactionship("City", back_populates='state', cascade="all, delete, save-update")

    def __init__(self, name=""):
        """
        State Constructor
        """
        self.name = name

    @property
    def cities(self):
        cities_list = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if city.state_id = self.id:
                cities_list.append(city)
        return cities_list
