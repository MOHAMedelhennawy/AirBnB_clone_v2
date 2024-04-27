#!/usr/bin/python3
"""Unittest User.
Test cases for User class.
"""


import unittest
import json
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestBase(unittest.TestCase):
    """
    Test class for User class
    """

    def setUp(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_userAttributes(self):
        """
        test if an object is instanciated correctly
        """
        user1 = User()
        user1.address = "milan"
        user1.save()
        self.assertEqual(user1.first_name, "")
        self.assertIsNotNone(user1.first_name)
        self.assertTrue(isinstance(user1, BaseModel))
        self.assertEqual(type(user1.email), str)
        self.assertEqual(type(user1.password), str)
        self.assertEqual(type(user1.first_name), str)
        self.assertEqual(type(user1.last_name), str)
        self.assertEqual(type(user1.id), str)
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.updated_at), datetime)
        self.assertEqual(user1.address, "milan")
        # test serialization and deserialization
        with open("file.json", 'r') as f:
            data_dict = json.load(f)
        key = "User.{}".format(user1.id)
        self.assertTrue(data_dict[key])
