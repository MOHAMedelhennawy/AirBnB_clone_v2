#!/usr/bin/python3
"""user class, subclass of BaseModel
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """
    A subclass of BaseModel class

    Public class attribute:
    email (str): user email
    password (str): user password
    first_name (str): user first_name
    last_name (str): user last_name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship('Place', backref='user', cascade='all, delete')
    reviews = relationship('Review', backref='user', cascade='all, delete')
