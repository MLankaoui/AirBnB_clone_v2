#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone."""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """
    Base class for all models in our hbnb clone.

    Attributes:
        id (str): The unique identifier for each instance.
        created_at (DateTime): The datetime when the instance was created.
        updated_at (DateTime): The datetime of the last update to the instance.
    """

    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        if not kwargs.get('id'):
            self.id = str(uuid.uuid4())
        else:
            self.id = kwargs['id']

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            kwargs['updated_at'] = kwargs.get('updated_at', datetime.now())
            kwargs['created_at'] = kwargs.get('created_at', datetime.now())
            if isinstance(kwargs['updated_at'], str):
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if isinstance(kwargs['created_at'], str):
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

            kwargs.pop('__class__', None)

            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: Formatted string with class name, instance id, and instance attributes.
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime and saves the instance.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Converts the instance into a dictionary representation.

        Returns:
            dict: Dictionary representation of the instance attributes.
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """
        Deletes the current instance from storage.
        """
        from models import storage
        storage.delete(self)
