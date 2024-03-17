#!/usr/bin/python3
"""
module that contain engine DBStorage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """
    class DBStorage

    Attributes:
    __engine: the engine
    __session: the session
    """
    __engine = None
    __session = None

