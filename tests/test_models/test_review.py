#!/usr/bin/python3
"""
Module to test  Review class
"""

import unittest
import json
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestReview(unittest.TestCase):

    """
    Test class for Review class
    """

    def setUp(self):
        """
        setup method in test review
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_review(self):
        """
        test object initialization in review class
        """
        obj_review = Review()
        self.assertFalse(os.path.exists("file.json"))
        obj_review.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertTrue(isinstance(obj_review, BaseModel))
        self.assertTrue(type(obj_review), Review)
        self.assertEqual(type(obj_review.id), str)
        self.assertEqual(type(obj_review.created_at), datetime)
        self.assertEqual(type(obj_review.updated_at), datetime)
        self.assertIsNotNone(obj_review.id)
        self.assertIsNotNone(obj_review.created_at)
        self.assertIsNotNone(obj_review.updated_at)
        self.assertIsNotNone(obj_review.place_id)
        self.assertIsNotNone(obj_review.user_id)
        self.assertIsNotNone(obj_review.text)
        self.assertIsInstance(obj_review.place_id, str)
        self.assertIsInstance(obj_review.user_id, str)
        self.assertIsInstance(obj_review.text, str)
        obj_review.satisfy = "yes"
        self.assertEqual(obj_review.satisfy, "yes")
        self.assertEqual(type(obj_review.satisfy), str)
        # test serialization and deserialization
        with open("file.json", 'r') as f:
            data_dict = json.load(f)
        key = "Review.{}".format(obj_review.id)
        self.assertTrue(bool(data_dict[key]))
