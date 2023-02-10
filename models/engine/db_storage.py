"""Defines a DBStorage class engine"""

from sqlalchemy import create_engine
from models.base_model import Base
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

user = getenv('HBNB_MYSQL_USER')
pwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
env = getenv('HBNB_ENV')

classes_db = {
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class DBStorage:
    """Represents a DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all()

    def all(self, cls=None):
        """query on the current database session"""
        my_objects = {}
        if not self.__session:
            self.reload()
        if type(cls) == str:
            cls = classes_db.get(cls, None)
        if cls is not None:
            for obj in self.__session.query(cls):
                my_objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in classes_db.values():
                for obj in self.__session.query(cls):
                    my_objects[obj.__class__.__name__ + '.' + obj.id] = obj
        return my_objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads all tables from the database"""
        Base.metadata.create_all(self.__engine)
        session_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_db)

    def close(self):
        """Sessions closed"""
        self.__session.remove()
