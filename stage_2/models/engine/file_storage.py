import json

from models.base_model import AllBaseModel
from models.person import Person


classes = {"AllBaseModel": AllBaseModel, "Person": Person}


class FileStorage:
    """Serializes instances to a JSON file and deserializes back to instances"""

    # String - path to the JSON file
    __file_path = "file.json"
    # Dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                self.__objects[key] = classes[value["__class__"]](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it’s inside"""
        if obj is not None:
            del self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]
            self.save()

    def close(self):
        """Deserializes JSON file to objects"""
        self.reload()

    def get(self, cls: Person, name: str):
        """Returns the object based on the class name and the person name, or None if not found"""
        if cls is not None and name is not None:
            for key, value in self.__objects.items():
                if name == value.name:
                    return value
        return None
