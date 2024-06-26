#!/usr/bin/python3
"""Place class."""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class Place(BaseModel, Base):
    __tablename__ = 'places'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
