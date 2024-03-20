#!/usr/bin/python3
"""
module that contain engine DBStorage
"""
import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
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
    classes_list = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def __init__(self):
        """ DB Storage constructor """
        usr = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        localhost = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        engine = 'mysql+mysqldb://{}:{}@{}/{}'.format(usr, password, localhost, db)
        self.__engine = create_engine(engine, pool_pre_ping=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        self.__session = Session()
        if env == "test":
            self.__session.drop_all()

    def all(self, cls=None):
        """ Returns all objects depending on the class name"""
        Filtered_classes = []
        classes_obj = {}

        if cls is None:
            for clas in classes_list.values():
                Filtered_classes.extend(self.__session.query(clas).all())

        elif cls != None and cls in classes_list.values():
            Filtered_classes.extend(self.__session.query(cls).all)

        for obj in Filtered_classes:
            key = obj.__class__.__name__ + '.' + obj.id
            classes_obj[key] = obj

        return classes_obj

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)
    
    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()
    
    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        reload the data from database
        """

        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    
    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove() 