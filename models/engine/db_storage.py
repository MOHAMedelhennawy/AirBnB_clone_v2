#!/usr/bin/python3
import os
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        values must be retrieved via environment variables
        """
        mysql_user = os.environ.get("HBNB_MYSQL_USER")
        mysql_passwd = os.environ.get("HBNB_MYSQL_PWD")
        mysql_host = os.environ.get("HBNB_MYSQL_HOST")
        mysql_database = os.environ.get("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(mysql_user, mysql_passwd,
                                              mysql_host, mysql_database),
                                      pool_pre_ping=True)

        if os.environ.get("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query all objects if cls is None,
        Otherwise query all objects depending of the class name
        """

        DBStorage_dict = {}
        if cls:
            filtered_query = self.__session.query(cls).all()
        else:
            filtered_query = self.__session.query(State).all()
            filtered_query.extend(self.__session.query(City).all())
            filtered_query.extend(self.__session.query(User).all())
            filtered_query.extend(self.__session.query(Place).all())
            filtered_query.extend(self.__session.query(Review).all())
            # filtered_query.extend(self.__session.query(Amenity).all())

        for query in filtered_query:
            key = type(query).__name__ + '.' + query.id
            DBStorage_dict[key] = query

        return DBStorage_dict

    def new(self, obj):
        """
        add the object to the current database session
        """

        self.__session.add(obj)
        self.save()

    def save(self):
        """
        commit all changes of the current database session
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
