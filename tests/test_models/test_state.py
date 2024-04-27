#!/usr/bin/python3
"""Unittest State.
Test cases for state class.
"""


import unittest
import json
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestState(unittest.TestCase):
    """
    Test class for State class
    """

    def setUp(self):
        """
        setup method for test state
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_state(self):
        """
        Test if file.json created successfully
        """

        state_obj = State()
        self.assertFalse(os.path.exists("file.json"))
        state_obj.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_attributes(self):
        """
        Test state class attribute
        """
        state_obj = State()
        state_obj.save()
        self.assertIsInstance(state_obj.name, str)
        self.assertIsNotNone(state_obj.name)
        self.assertIsInstance(state_obj, State)
        self.assertTrue(isinstance(state_obj, BaseModel))
        state_obj.save()
        self.assertEqual(state_obj.name, "")
        self.assertIsInstance(state_obj, State)
        self.assertTrue(isinstance(state_obj, BaseModel))
        self.assertIsNotNone(state_obj.id)
        self.assertIsInstance(state_obj.id, str)
        self.assertEqual(type(state_obj.created_at), datetime)
        self.assertEqual(type(state_obj.updated_at), datetime)
        self.assertIsNotNone(state_obj.created_at)
        self.assertIsNotNone(state_obj.updated_at)
        with open("file.json", 'r') as f:
            data_dict = json.load(f)
        key = "State.{}".format(state_obj.id)
        self.assertTrue(bool(data_dict[key]))
