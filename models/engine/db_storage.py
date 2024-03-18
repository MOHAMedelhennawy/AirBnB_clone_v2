#!/usr/bin/python3
"""
module that contain engine DBStorage
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_model import Base, BaseModel
from city import City
from state import State
from user import User
from place import Place
from review import Review


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
        """ DB Storage constructor """
        usr = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        localhost = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        en = 'mysql+mysqldb://{}:{}@{}/{}'.format(usr, password, localhost, db)
        self.__engine = create_engine(en, pool_pre_ping=True)
        # Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.__session = Session()
        if env == "test":
            self.__session.drop_all()

    def all(self, cls=None):
        """ Returns all objects depending on the class name"""
        if cls:

