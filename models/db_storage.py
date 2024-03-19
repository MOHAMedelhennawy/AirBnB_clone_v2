#!/usr/bin/python3
"""
module that contain engine DBStorage
"""
from os import getenv
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

    def __init__(self):
        user =  getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
        .format(user, password, host, database), pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    
    all(self, cls=None):
        