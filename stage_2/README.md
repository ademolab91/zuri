# ZURI INTERSHIP STAGE 2 TASK (BACKEND)

A simple REST API capable of CRUD operations on a resource, say in this case, a "person".

Use the service here: [https://stage-2.onrender.com/docs#/](https://stage-2.onrender.com/docs#/)

See the [UML Diagram](https://drive.google.com/file/d/15rEQLyQyFp440u-oL7wEfS-FanfdY0Yd/view?usp=drivesdk)

## Setup Instructions

Make sure you have [poetry](https://python-poetry.org) installed before going on!

1. `git clone https://github.com/ademolab91/stage_2`
2. Change directory `cd stage_2`
3. Run `poetry install`
4. Then, run `STAGE_2_STORAGE_TYPE=db uvicorn main:app`. For using json file storage, run `uvicorn main:app`

## Usage

See [DOCUMENTATION.md](https://github.com/ademolab91/zuri/blob/main/stage_2/DOCUMENTATION.md)

## Testing

To test the endpoint, run `pytest tests/test_person.py`
