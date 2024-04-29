#!/usr/bin/python3
"""
Amenity class, a subclass of BaseModel
"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """
    A subclass of BaseModel class
    Public class attribute:
        name: (str)
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
