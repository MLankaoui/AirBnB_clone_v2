#!/usr/bin/python3
"""
DBStorage Module for SQL Alchemy Configuration

This module defines a class `DBStorage` that configures SQLAlchemy for a MySQL database.

Classes:
    DBStorage: A class that manages SQLAlchemy configurations and database operations.

Usage:
    To use DBStorage:
    1. Instantiate the DBStorage class.
    2. Call methods like `all()`, `new()`, `delete()`, `save()`, `reload()`, and `close()` as needed.
"""
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
    """
    DBStorage class for configuring SQLAlchemy with a MySQL database.

    Attributes:
        __engine (Engine): SQLAlchemy Engine instance for database connection.
        __session (Session): SQLAlchemy Session instance for database interactions.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a DBStorage instance with SQLAlchemy Engine configuration.

        The initialization connects to the MySQL database specified by environment
        variables HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, and HBNB_MYSQL_DB.
        If HBNB_ENV is set to "test", it drops all tables in the database.

        Args:
            None

        Returns:
            None
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")
        ), pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of objects in the current session.

        Args:
            cls (class, optional): Class of objects to query. If None, queries all specified classes.

        Returns:
            dict: Dictionary of objects mapped by '<class name>.<object id>'
        """
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
            for clase in ls:
                qr = self.__session.query(clase)
                for el in qr:
                    k = "{}.{}".format(type(el).__name__, el.id)
                    dc[k] = el
        return (dc)

    def new(self, obj):
        """
        Adds a new object to the current session.

        Args:
            obj (BaseModel): Object to add to the session.

        Returns:
            None
        """
        self.__session.add(obj)

    def save(self):
        """
        Saves changes in the current session.

        Args:
            None

        Returns:
            None
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current session.

        Args:
            obj (BaseModel, optional): Object to delete from the session.

        Returns:
            None
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """
        Configures a new session with the current engine and reloads data from the database.

        Args:
            None

        Returns:
            None
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """
        Closes the current session.

        Args:
            None

        Returns:
            None
        """
        self.__session.close()
