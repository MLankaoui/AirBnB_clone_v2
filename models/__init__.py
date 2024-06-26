#!/usr/bin/python3
"""
Unique storage instance initialization for your application.

This script initializes a unique storage instance based on the environment
variable 'HBNB_TYPE_STORAGE'.
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


# Determine the type of storage based on the environment variable
if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload any stored data into the storage instance
storage.reload()
