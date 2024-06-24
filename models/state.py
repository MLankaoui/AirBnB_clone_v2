#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


class State(BaseModel, Base):
    """ State class representing states in the application. """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
