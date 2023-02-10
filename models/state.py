#!/usr/bin/python3
""" State Module for HBNB project """

import sqlalchemy
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ getter attribute cities that returns the list of city """
            cities_list = []
            cities = models.storage.all('City').values()
            for city in cities:
                if self.id == city.state_id:
                    cities_list.append(city)
            return cities_list
