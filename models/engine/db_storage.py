#!/usr/bin/python3
"""Defines the DBStorage engine"""
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

class DBStorage:
    """the db strorage
    Attribute:
    __engine: the working sqalchemy engine
    __session: the working sqalchemy session
    """

    __engine = None
    __session = None
    def __init__self:
        """creates a new db storage instance """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
                pool_pre_ping=True)
        if getenve("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        if cls is none, queries all types of objects
        Return: dictionary of qualified classes
        """
        if cls is None:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls + eval(cls)
            objects = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objects)
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)
    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy)
        """
        Base.metadta.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                expire_on_commit=False)
        session = scoped_session(session_factory)
        self._session = Session()

    def close(self):
        """
        closes the working sqlalchemy session
        """
        self.session.close()
