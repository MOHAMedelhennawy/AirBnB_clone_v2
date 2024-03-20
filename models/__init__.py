#!/usr/bin/python3
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine import db_storage
    storage = db_storage.DBStorage()
    storage.reload()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()
    storage.reload()
