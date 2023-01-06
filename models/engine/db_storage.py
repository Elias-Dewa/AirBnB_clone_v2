"""Defines a DBStorage class engine"""

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

classes = {
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
            user, pwd, host, db), pool_pre_ping=True
        )
    if env == 'test':
        Base.metadata.drop_all()

    def all(self, cls=None):
        """query on the current database session"""
        if cls is not None:
            objects = self.__session.query(eval(cls)).all()
        else:
            objects = self.__session.query(User).all()
            objects += self.__session.query(State).all()
            objects += self.__session.query(City).all()
            objects += self.__session.query(Amenity).all()
            objects += self.__session.query(Place).all()
            objects += self.__session.query(Review).all()
        my_dict = {}
        for obj in objects:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_db)
        self.__session = Session()

    def close(self):
        """Sessions closed"""
        self.__session.close()
