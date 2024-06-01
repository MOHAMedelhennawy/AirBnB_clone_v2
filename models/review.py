#!/usr/bin/python3
"""
Review class, a subclass of BaseModel class
"""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
import os

class Review(BaseModel, Base):
    """
    A subclass of BaseModel class
    Public class attributes:
        place_id:            (str) will be Place.id
        user_id:             (str) will be User.id
        text:                (str)
    """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':

        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)