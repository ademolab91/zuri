import models
from models.base_model import AllBaseModel


class Person(AllBaseModel, table=True):
    """Person model"""

    name: str
