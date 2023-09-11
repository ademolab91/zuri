# DOCUMENTATION

## UML Diagram

See [https://drive.google.com/file/d/15rEQLyQyFp440u-oL7wEfS-FanfdY0Yd/view](here)

## Format

- POST `/add` - Endpoint for adding a user to the database
  - body: {
    "name": "Mark Essien"
    }
  - response: {
    "id": "12hdfjksj-fajs76jev3-hdjs7-ysjosowu"
    "name": "Mark Essien"
    }
  - response status code: 201
- GET `/read` - Endpoint for getting a user from the database
  - body: {
    "name": "Mark Essien"
    }
  - response: {
    "id": "12hdfjksj-fajs76jev3-hdjs7-ysjosowu"
    "name": "Mark Essien"
    }
  - response status code: 200
- PATCH `/update` - Endpoint for editing a user in the database
  - body: {
    "name": "Mark Essien"
    "new_name": "Kram Neisse"
    }
  - response: {
    "id": "12hdfjksj-fajs76jev3-hdjs7-ysjosowu"
    "name": "Kram Neisse"
    }
  - response status code: 202
- DELETE `/remove` - Endpoint for removing a user from the database
  - body: {
    "name": "Kram Neisse"
    }
  - response status code: 200

## Setup Instructions

Make sure you have [https://python-poetry.org](poetry) installed before going on!

1. `git clone https://github.com/ademolab91/stage_2`
2. Chande directory `cd stage_2`
3. Run `poetry install`
4. Then, run `STAGE_2_STORAGE_TYPE=db uvicorn main:app` for using json file storage, run `uvicorn main:app`
