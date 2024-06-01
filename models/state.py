#!/usr/bin/python3
"""
State class, a subclass of BaseModel
"""


from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """
    A subclass of BaseModel class

    Public class attribute:
    name (str): state name
    """ 
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Returns the list of City instances with state_id
            equals to the current State.id
            """
            from models.engine import file_storage
            cities_list = []
            all_cities = file_storage.FileStorage.all(City)
            for city in all_cities.values():
                if isinstance(city, City) and city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
