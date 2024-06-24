#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from models import storage

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
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
        """Returns a string representation of the instance"""
        c = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(c, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        d__i_ct = {}
        d__i_ct.update(self.__dict__)
        d__i_ct.update({'__class__':
                        (str(type(self)).split('.')[-1]).split('\'')[0]})
        d__i_ct['created_at'] = self.created_at.isoformat()
        d__i_ct['updated_at'] = self.updated_at.isoformat()

        if '_sa_instance_state' in d__i_ct:
            del d__i_ct['_sa_instance_state']

        return d__i_ct

    def delete(self):
        """ Deletes current instance from storage """
        storage.delete(self)
