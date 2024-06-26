#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """
    Review class to store review information.


    Attributes:
        __tablename__ (str): Database table name for reviews.
        text: Review content stored as a string.
        place_id: Foreign key referencing places.id.
        user_id: Foreign key referencing users.id.
    """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
