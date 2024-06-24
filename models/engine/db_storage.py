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
    
        