from datetime import datetime
from uuid import uuid4
from sqlmodel import SQLModel, Field

import models


TIME: str = "%Y-%m-%dT%H:%M:%S.%f"


def generate_uuid():
    """Generate UUID"""
    return str(uuid4())


class AllBaseModel(SQLModel):
    """Base model for all models"""

    id: str = Field(default_factory=generate_uuid, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __str__(self) -> str:
        """String representation of the BaseModel"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.strftime(TIME)
        new_dict["updated_at"] = self.updated_at.strftime(TIME)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
