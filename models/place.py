#!/usr/bin/python3
"""
Place class, a subclass of BaseModel class
"""
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """
    A subclass of BaseModel class
    Public class attributes:
        city_id:             (str) will be City.id
        user_id:             (str) will be User.id
        name:                (str)
        description:         (str)
        number_rooms:        (int) 0
        number_bathrooms:    (int) 0
        max_guest:           (int) 0
        price_by_night:      (int) 0
        latitude:            (float) 0.0
        longitude:           (float) 0.0
        amenity_ids:         (list) will be Amenity.id
    """
    # city_id = ""
    # user_id = ""
    # name = ""
    # description = ""
    # number_rooms = 0
    # number_bathrooms = 0
    # max_guest = 0
    # price_by_night = 0
    # latitude = 0.0
    # longitude = 0.0
    # amenity_ids = []

    __tablename__ = "places"
    city_id = Column(String(60),ForeignKey('cities.id') , nullable=False)
    user_id = Column(String(60),ForeignKey('users.id') , nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    