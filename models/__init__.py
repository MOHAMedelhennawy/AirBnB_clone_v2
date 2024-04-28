#!/usr/bin/python3

from models.engine import file_storage, db_storage
import os

if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
    storage = db_storage.DBStorage()
else:
    storage = file_storage.FileStorage()

storage.reload()
