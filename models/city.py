from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'
    
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    
    # Relationship with Place
    places = relationship('Place', backref='cities', cascade='all, delete-orphan')

