#!/usr/bin/python3
"""
Module to test Place class
"""

import unittest
import json
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestPlace(unittest.TestCase):

    """
    Test class for Place class
    """

    def setUp(self):
        """
        setup method in test place
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_place(self):
        """
        test object initialization in place class
        """
        obj_place = Place()
        self.assertFalse(os.path.exists("file.json"))
        obj_place.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertIsInstance(obj_place, BaseModel)
        self.assertIsInstance(obj_place, Place)
        self.assertIsInstance(obj_place.id, str)
        self.assertIsInstance(obj_place.created_at, datetime)
        self.assertIsInstance(obj_place.updated_at, datetime)
        self.assertIsInstance(obj_place.city_id, str)
        self.assertIsInstance(obj_place.user_id, str)
        self.assertIsInstance(obj_place.name, str)
        self.assertIsInstance(obj_place.description, str)
        self.assertIsInstance(obj_place.number_rooms, int)
        self.assertIsInstance(obj_place.number_bathrooms, int)
        self.assertIsInstance(obj_place.max_guest, int)
        self.assertIsInstance(obj_place.price_by_night, int)
        self.assertIsInstance(obj_place.latitude, float)
        self.assertIsInstance(obj_place.longitude, float)
        self.assertIsInstance(obj_place.amenity_ids, list)
        self.assertIsNotNone(obj_place.id)
        self.assertIsNotNone(obj_place.created_at)
        self.assertIsNotNone(obj_place.updated_at)
        self.assertIsNotNone(obj_place.city_id)
        self.assertIsNotNone(obj_place.user_id)
        self.assertIsNotNone(obj_place.name)
        self.assertIsNotNone(obj_place.description)
        self.assertIsNotNone(obj_place.number_rooms)
        self.assertIsNotNone(obj_place.number_bathrooms)
        self.assertIsNotNone(obj_place.max_guest)
        self.assertIsNotNone(obj_place.price_by_night)
        self.assertIsNotNone(obj_place.latitude)
        self.assertIsNotNone(obj_place.longitude)
        self.assertIsNotNone(obj_place.amenity_ids)

        obj_place.location = "fifth"
        self.assertEqual(obj_place.location, "fifth")
        self.assertEqual(type(obj_place.location), str)
        # test serialization and deserialization
        with open("file.json", 'r') as f:
            data_dict = json.load(f)
        key = "Place.{}".format(obj_place.id)
        self.assertTrue(bool(data_dict[key]))
