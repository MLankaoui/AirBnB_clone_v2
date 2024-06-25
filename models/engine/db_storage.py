#!/usr/bin/python3
""" new class for sqlAlchemy """
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")
        ),pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dc = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            qr = self.__session.query(cls)
            for el in qr:
                k = "{}.{}".format(type(el).__name__, el.id)
                dc[k] = el
        else:
            ls = [State, City, User, Place, Review, Amenity]
            for clase in dc:
                qr = self.__session.query(clase)
                for el in qr:
                    k = "{}.{}".format(type(el).__name__, el.id)
                    dc[k] = el
        return (dc)
    
    def new(self, obj):
        self.__session.add(obj)


    def delete(self, obj=None):
        if obj:
            self.session.delete()

    
    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ close session """
        self.__session.close()

