#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
class Place(BaseModel, Base):
    """ represents a place for a mysql database """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(120), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenities = relationship("Amentity", secondary="place_amentity", viewonly=False)
    reviews = relationship("Review", backref="place", cascade="delete")

    amenity_ids = []
    overlaps = "place_amenities"
    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """gets a list all linked reviews"""
            review_list = []
            for rev in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list,append(rev)
            return review_list

        @property
        def amenities(self):
            """set linked amenities"""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.ammenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, values):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
    



