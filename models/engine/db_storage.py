#!/usr/bin/python3
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        mysql_user = os.environ.get("HBNB_MYSQL_USER")
        mysql_passwd = os.environ.get("HBNB_MYSQL_PWD")
        mysql_host = os.environ.get("HBNB_MYSQL_HOST")
        mysql_database = os.environ.get("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(mysql_user, mysql_passwd,
                                              mysql_host, mysql_database),
                                              pool_pre_ping=True)

        if os.environ.get("HBNB_ENV") == 'test':
            Base.metadata.drop_all()


    def all(self, cls=None):
        """
        query all objects if cls is None,
        Otherwise query all objects depending of the class name
        """

        DBStorage_dict = {}
        if cls:
            filtered_query = self.__session.query(cls).all()
        else:
            filtered_query = self.__session.query(Base).all()
        
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
        Base.metadata.create_all(self.__engine)


        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()