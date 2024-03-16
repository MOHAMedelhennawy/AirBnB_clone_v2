#!/usr/bin/python3
"""Unittest User.
Test cases for Amenity class.
"""


import unittest
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestAmenity(unittest.TestCase):
    """
    Test class for Amenity class
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

    def test_amenity(self):
        """
        Test if file.json created successfully
        """

        amenity_obj = Amenity()
        self.assertFalse(os.path.exists("file.json"))
        amenity_obj.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_attributes(self):
        """
        Test state amenity class attribute
        """
        amenity_obj = Amenity()
        amenity_obj.name = "Betty"
        amenity_obj.save()
        self.assertEqual(amenity_obj.name, "Betty")
        self.assertIsInstance(amenity_obj, Amenity)
        self.assertTrue(isinstance(amenity_obj, BaseModel))
        self.assertIsInstance(amenity_obj.name, str)
        self.assertIsNotNone(amenity_obj.id)
        self.assertIsInstance(amenity_obj.id, str)
        self.assertEqual(type(amenity_obj.created_at), datetime)
        self.assertEqual(type(amenity_obj.updated_at), datetime)
        self.assertIsNotNone(amenity_obj.created_at)
        self.assertIsNotNone(amenity_obj.updated_at)
        amenity_obj2 = Amenity(name="My_First_Name", my_number=43)
        self.assertEqual(amenity_obj2.name, "My_First_Name")
        self.assertIsInstance(amenity_obj2.name, str)
        self.assertEqual(amenity_obj2.my_number, 43)
        self.assertIsInstance(amenity_obj2.my_number, int)
        with open("file.json", 'r') as f:
            data_dict = json.load(f)
        key = "Amenity.{}".format(amenity_obj.id)
        self.assertTrue(bool(data_dict[key]))
