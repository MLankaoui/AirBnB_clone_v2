#!/usr/bin/python3
""" State Module for HBNB project """
import shlex
import models
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

Base = declarative_base()
STORAGE_TYPE = os.environ.get("HBNB_TYPE_STORAGE")



class State(BaseModel, Base):
    """
    State class representing states in the application.

    Attributes:
        __tablename__ (str): Name of the database table for states.
        name (str): Name of the state.
        cities (relationship): One-to-many relationship to the City model.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
    

    @property
    def cities(self):
        """
        Getter property for cities related to the current state.

        Returns:
            list: List of City objects associated with the current state.
        """
        if STORAGE_TYPE != 'db':
            v = models.storage.all()
            ls = []
            rs = []

            for k in v:
                city = k.replace('.', ' ')
                city = shlex.split(city)

                if city[0] == 'City':
                    ls.append(v[k])
            for el in ls:
                if el.state_id == self.id:
                    rs.append(el)

            return rs
        
        else:
            return [city for city in self.cities]
