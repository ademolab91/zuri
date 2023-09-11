import models
from models.person import Person


def create_person():
    """Return the instance of a string representation of a person

    >>> person = Person(id=id, name="Mark Essien")
    >>> person.save()
    >>> db_person = models.storage.get(Person, person.name)
    >>> person.id == db_person.id
    True

    """
    pass


if __name__ == "__main__":
    import doctest

    create_person()

    doctest.testmod()
