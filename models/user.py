#!/usr/bin/python3
"""User class."""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    reviews = relationship('Review', cascade='all, delete', backref='user')
    places = relationship('Place', cascade='all, delete', backref='user')
