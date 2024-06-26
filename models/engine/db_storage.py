#!/usr/bin/python3

""" """

from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """
    """
    _engine = None
    _session = None

    def __init__(self):
        """
        """
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(username, password, host, db_name)
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self._engine)

    def all(self, cls=None):
        """
        """
        objs_list = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                objs_list = self.__session.query(cls).all()
        else:
            for subclass in Base._subclasses_():
                objs_list.extend(self.__session.query(subclass).all())
        obj_dict = {}
        for obj in objs_list:
            key = "{}.{}".format(obj.__class__.name__.obj.id)
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        ""
        self.__session.add(obj)

    def save(self):
        ""
        self.__session.commit()

    def delete(self, obj=None):
        ""
        self.__session.delete(obj)
    
    def reload(self):
        ""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Sessiom()
