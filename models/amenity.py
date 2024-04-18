#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import reletionship


class Amenity(BaseModel):
    """represents an amenity for a MYSQL database"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amentities + relationship("place", secondary+"place_amenity", viewonly=False)
