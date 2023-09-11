from __future__ import annotations

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

import models
from models.person import Person


class PersonIn(BaseModel):
    """Person in model"""

    name: str


class PersonOut(PersonIn):
    """Person out model"""

    id: str


class PersonUpdate(PersonIn):
    """Person update model"""

    new_name: str


def parse_name(person: PersonIn | PersonUpdate):
    """Check the name of a person and Capitalize the name of a person"""

    person.name = person.name.strip()
    name = person.name.split()
    for n in name:
        if not n.isalpha():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You dey whine me abi. Alaye, enter correct name joor",
            )
    if person.__class__.__name__ == "PersonUpdate":
        person.new_name = person.new_name.strip()
        new_name = person.new_name.split()
        for n in new_name:
            if not n.isalpha():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="You dey whine me abi. Alaye, enter correct new name joor",
                )
        new_name = [n.capitalize() for n in new_name]
        person.new_name = " ".join(new_name)
    name = [n.capitalize() for n in name]
    person.name = " ".join(name)

    return person


app = FastAPI()


@app.post("/api/add", status_code=status.HTTP_201_CREATED)
def add_person(person: PersonIn) -> PersonOut:
    """Add Person"""

    person = parse_name(person)
    person: Person = Person(name=person.name)
    person.save()
    print(person)
    return person


@app.get("/api/read", status_code=status.HTTP_200_OK)
def get_person(person: PersonIn) -> PersonOut:
    """Get a person"""

    person = parse_name(person)
    person: Person = models.storage.get(Person, person.name)
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return person


@app.patch("/api/update", status_code=status.HTTP_202_ACCEPTED)
def update_person(person: PersonUpdate) -> PersonOut:
    """Update a person"""

    person = parse_name(person)
    db_person: Person = models.storage.get(Person, person.name)
    if not db_person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db_person.name = person.new_name
    db_person.save()
    print(db_person)
    return db_person


@app.delete("/api/remove", status_code=status.HTTP_200_OK)
def remove_person(person: PersonIn) -> None:
    """Remove a person"""

    person = parse_name(person)
    db_person: Person = models.storage.get(Person, person.name)
    if not db_person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db_person.delete()
    return None
