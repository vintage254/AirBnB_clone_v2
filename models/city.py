#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.com import relationship

class City(BaseModel):
    """ inherits from sqlalchemy base and links to the MYAQL table cities
    The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(string(128), nullable=False)
    state_id = Column(string(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
