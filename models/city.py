#!/usr/bin/python3
""" City Module for the HBNB project. """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """
    City class representing cities in the application.

    Attributes:
        __tablename__ (str): Name of the database table for cities.
        state_id (str): Foreign key to the 'id' column of the 'states' table.
        name (str): Name of the city.
        places (relationship): Relationship to the Place model.
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship(
        "Place",
        cascade="all, delete, delete-orphan",
        backref="cities")
