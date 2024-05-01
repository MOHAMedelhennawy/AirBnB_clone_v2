#!/usr/bin/python3
"""Unittest base.
Test cases for FileStorage class.
"""

import unittest
import os
from time import sleep
import datetime
import json
import models
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test class for FileStorage class."""

    def setUp(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_FileStorage(self):
        """
        Test FileStorage attributes
        """

        self.assertIsInstance(FileStorage(), FileStorage)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(storage, FileStorage)
        with self.assertRaises(TypeError) as Err_msg:
            obj_Test = FileStorage("This arg")
    
    def test_deleted_file(self):
        """
        Test that file deleted successfully
        """

        self.assertFalse(os.path.exists("file.json"))

    def test_attributes(self):
        """
        Test FileStorage class attribute
        """
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertEqual(FileStorage._FileStorage__objects, {})
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all(self):
        """
        Test all method
        """
        fs = FileStorage()
        all_objs = fs.all()
        self.assertEqual(all_objs, {})
        self.assertIsInstance(all_objs, dict)
        self.assertFalse(os.path.exists("file.json"))
        self.assertEqual(len(all_objs), 0)

        # Create a new State
        new_state = State()
        new_state.name = "California"
        fs.new(new_state)
        fs.save()
        all_states = fs.all(State)
        all_objects = fs.all()
        self.assertEqual(len(all_states), 1)
        self.assertEqual(len(all_objects), 1)

        another_state = State()
        another_state.name = "Nevada"
        fs.new(another_state)
        fs.save()
        all_states = fs.all(State)
        all_objects = fs.all()
        self.assertEqual(len(all_states), 2)
        self.assertEqual(len(all_objects), 2)

        new_city = City()
        new_city.name = "San_Francisco"
        fs.new(new_city)
        fs.save()
        all_cities = fs.all(City)
        all_objects = fs.all()
        self.assertEqual(len(all_cities), 1)
        self.assertEqual(len(all_objects), 3)

        new_user = User()
        new_user.first_name = "Guillaume"
        new_user.last_name = "Snow"
        fs.new(new_user)
        fs.save()
        all_users = fs.all(User)
        all_objects = fs.all()
        self.assertEqual(len(all_users), 1)
        self.assertEqual(len(all_objects), 4)

    def test_save(self):
        """
        Test save method
        """

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(os.path.exists("file.json"))
        all_objs = storage.all()
        self.assertNotEqual(all_objs, {})
        self.assertEqual(len(all_objs), 1)
        self.assertNotEqual(len(all_objs), 0)
        with self.assertRaises(TypeError) as msg:
            my_model.save("This arg")

        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + my_model.id, save_text)

    def test_new(self):
        """
        Test new method
        """
        my_model = BaseModel()
        self.assertTrue(bool(FileStorage._FileStorage__objects))
        self.assertNotEqual(FileStorage._FileStorage__objects, {})
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_reload(self):
        """
        Test reload method
        """
        my_model = BaseModel()
        my_model.save()
        storage = FileStorage()
        all_objs = storage.all()
        obj = all_objs['BaseModel.{}'.format(my_model.id)]
        self.assertEqual(obj, my_model)
        my_model1 = BaseModel()
        my_model1.save()
        all_objs = storage.all()
        obj = all_objs['BaseModel.{}'.format(my_model.id)]
        obj1 = all_objs['BaseModel.{}'.format(my_model1.id)]
        self.assertNotEqual(all_objs, {})
        self.assertEqual(len(all_objs), 2)
        self.assertNotEqual(len(all_objs), 0)
        with self.assertRaises(TypeError) as msg:
            storage.reload("This arg")

        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_delete(self):
        """
        Test delete methode
        """

        fs = FileStorage()
        all_states = fs.all(State)
        self.assertEqual(len(all_states), 0)

        # Create a new State
        new_state = State()
        new_state.name = "California"
        fs.new(new_state)
        fs.save()
        all_states = fs.all(State)
        self.assertEqual(len(all_states), 1)

        # Create another State
        another_state = State()
        another_state.name = "Nevada"
        fs.new(another_state)
        fs.save()
        all_states = fs.all(State)
        self.assertEqual(len(all_states), 2)

        # Delete state object
        fs.delete(new_state)
        all_states = fs.all(State)
        self.assertEqual(len(all_states), 1)

if __name__ == '__main__':
    unittest.main()
