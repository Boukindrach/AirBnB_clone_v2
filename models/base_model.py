#!/usr/bin/python3
"""BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime
import os
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """BaseModel class for other models to inherit from."""

    id = Column(String(60), nullable = False, primary_key = True)
    created_at = Column(DateTime, nullable = False, default = datetime.utcnow())
    updated_at = Column(DateTime, nullable = False, default = datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs and "id" not in self.__dict__:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        elif kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """Save the instance to storage."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Convert instance to dictionary."""
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """Return string representation of the instance."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)
