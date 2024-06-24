#!/usr/bin/python3
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel

Base = declarative_base()


class User(BaseModel, Base):
    """
    User class that inherits from BaseModel.

    Attributes:
        __tablename__ (str): The name of the database
        table associated with this model.
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
