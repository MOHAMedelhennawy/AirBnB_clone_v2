#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State


# Create a new State
new_state = State()
print(type(new_state).__name__)