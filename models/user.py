#!/usr/bin/python3
"""user class, subclass of BaseModel
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import Relationship
from models.base_model import BaseModel, Base
import json


class User(BaseModel, Base):
    '''subclass of BaseModel class'''

    # email = ""
    # password = ""
    # first_name = ""
    # last_name = ""

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    cities = Relationship('Place', backref='user', cascade='all, delete')
    reviews = Relationship('Review', backref='user', cascade='all, delete')
