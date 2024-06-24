#!/usr/bin/python3
""" City Module for HBNB project. """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey

Base = declarative_base()


class City(BaseModel, Base):
    """ City class representing cities in the application. """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
