#!/usr/bin/python3
"""
Module to test city class
"""

import unittest
import json
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestCity(unittest.TestCase):

    """
    Test class for City class
    """

    def setUp(self):
        """
        setup method in test city
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_city(self):
        """
        test object initialization in city class
        """
        obj_city = City()
        self.assertFalse(os.path.exists("file.json"))
        obj_city.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertTrue(isinstance(obj_city, BaseModel))
        self.assertTrue(type(obj_city), City)
        self.assertEqual(type(obj_city.id), str)
        self.assertEqual(type(obj_city.created_at), datetime)
        self.assertEqual(type(obj_city.updated_at), datetime)
        self.assertIsNotNone(obj_city.id)
        self.assertIsNotNone(obj_city.created_at)
        self.assertIsNotNone(obj_city.updated_at)
        self.assertIsNotNone(obj_city.state_id)
        self.assertIsNotNone(obj_city.name)
        self.assertEqual(type(obj_city.state_id), str)
        self.assertEqual(type(obj_city.name), str)
        obj_city.location = "south"
        self.assertEqual(obj_city.location, "south")
        self.assertEqual(type(obj_city.location), str)
        # test serialization and deserialization
        with open("file.json", 'r') as f:
            data_dict = json.load(f)
        key = "City.{}".format(obj_city.id)
        self.assertTrue(bool(data_dict[key]))
