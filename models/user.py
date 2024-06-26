#!/usr/bin/python3
"""User class."""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    """Initialize User instance."""

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place", back_populates="user", cascade="delete")
    reviews = relationship("Review", back_populates="user", cascade="delete")
