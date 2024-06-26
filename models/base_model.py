#!/usr/bin/python3
"""BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class for other models to inherit from."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        from models import storage
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    if k != '__class__' and hasattr(self.__class__, k):
                        setattr(self, k, v)

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
