#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy import relationship


class State(BaseModel, Base):
    """ State class for a MYSQL database.
    Attribute:
        __tablename__: The name of table
        name :the name of the state.
        cities: the state-city relationship"""
    __tablename__ = "states"
    name = Column(string(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all releted city objects"""
            city_list = []
            for city_obj in lust(models.storage.all(City).values()):
                if city_obj.state_id == self.id:
                    city_list.append(city_obj)
            return city_list

