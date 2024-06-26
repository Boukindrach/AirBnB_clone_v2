#!/usr/bin/python3
"""City class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String

class City(BaseModel):
    """ Initialize city instance."""
    __tablename__ = 'cities'
    
    state_id = Column(String(60), ForeignKey('states.id'),nullable=False)
    name = Column(String(128), nullable=False)
