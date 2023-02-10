#!/usr/bin/python3
""" State Module for HBNB project """

import sqlalchemy
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Representation of amenity class"""
    __tablename__ = 'amenities'
    name = Column(String(128),
                  nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
