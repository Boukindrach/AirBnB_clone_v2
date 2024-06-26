#!/usr/bin/python3
"""State class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import os


class State(BaseModel):
    """Initialize State instance."""

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='delete')

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def all_cities(self):
            """
            getter for cities
            """
            cities = []
            insta = storage.all(City)
            for value in insta.values():
                if value.state_id == self.id:
                    cities.append(value)
            return cities
