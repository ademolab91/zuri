import os

table: bool = False

if os.getenv("STAGE_2_STORAGE_TYPE") == "db":
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    table = True
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    table = False
storage.reload()
