#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import place_amenity

Base = declarative_base()


class Amenity(BaseModel, Base):
    """
    Class for Amenity
    Attribute:
        name = input name
    """
    __tablename__ = 'amenities'
    name = Column(str(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity)
