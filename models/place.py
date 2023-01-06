#!/usr/bin/python3
""" Place Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv
place_amenity = Table(
    "place_amenity", Base.metadata,
    Column(
        "place_id", String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Reviews", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity,
                             backref="place_amenities", viewonly=False)

    amenity_ids = []

    @property
    def reviews(self):
        """getter attribute reviews that returns the list of Review
        instances with place_id equals to the current Place.id"""
        review_list = []
        reviews = models.storage.all(Review).values()
        for review in reviews:
            if self.id == review.place_id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """Getter attribute amenities that returns the list of Amenity
        instances based on the attribute amenity_ids"""
        amenity_list = []
        amenities = models.storage.all(Amenity).values()
        for amen in amenities:
            if self.id == amen.amenity_ids:
                amenity_list.append(amen)
        return amenity_list

    @amenities.setter
    def amenities(self, value):
        if type(value) == Amenity:
            self.amenity_id.append(value.id)
