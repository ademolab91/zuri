import requests


def test_person():
    """Test Person"""

    url = "https://stage-2.onrender.com"

    # Test add person
    person = {"name": "  john doe  "}
    response = requests.post(f"{url}/add", json=person)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

    # Test get person by name
    response = requests.get(f"{url}/read", json={"name": "John Doe"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

    # Test update person
    person = {"name": "  john doe  ", "new_name": "  jane doe  "}
    response = requests.patch(f"{url}/update", json=person)
    assert response.status_code == 202
    assert response.json()["name"] == "Jane Doe"

    # Test delete person
    person = {"name": "  jane doe  "}
    response = requests.delete(f"{url}/remove", json=person)
    assert response.status_code == 200
    assert response.json() is None


if __name__ == "__main__":
    test_person()
