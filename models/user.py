#!/usr/bin/python3
"""user class, subclass of BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    '''subclass of BaseModel class'''

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    def __init__(self, email="", password="", first_name="", last_name=""):
        """
        User Constructor
        """
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
