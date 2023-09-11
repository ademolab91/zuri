from sqlmodel import create_engine, Session, SQLModel

from models.base_model import AllBaseModel
from models.person import Person


classes = {"AllBaseModel": AllBaseModel, "Person": Person}


class DBStorage:
    """Interacts with the SQLITE database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine("sqlite:///database.db")

    def all(self, cls=None) -> dict:
        """Query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    new_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Reload all tables in the database and create the current database session"""
        SQLModel.metadata.create_all(self.__engine)
        self.__session = Session(self.__engine)

    def close(self):
        """Close the current database session"""
        self.__session.remove()

    def get(self, cls: Person, name: str) -> Person:
        """Returns the object based on the class name and name of the person, or None if not found"""
        return self.__session.query(cls).filter(cls.name == name).first()
