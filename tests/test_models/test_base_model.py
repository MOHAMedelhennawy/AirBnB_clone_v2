#!/usr/bin/python3
"""Unittest base.
Test cases for BaseModel class.
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel class."""

    def test_base(self):
        """
        Testing for BaseModel attributes
        """

        # Check that object working well and the same type of class
        my_model = BaseModel()
        my_model2 = BaseModel()

        # Checking that two object not equal
        flag = (my_model == my_model2)
        self.assertFalse(flag, False)

        flag = (my_model is my_model2)
        self.assertFalse(flag, False)

        # Checking the type of object
        self.assertEqual(type(my_model), BaseModel)
        flag = (type(my_model) == type(my_model2))
        self.assertTrue(flag, True)

        flag = (isinstance(my_model, BaseModel))
        self.assertTrue(flag, True)

    def test_id(self):
        '''
        Test id attribute of class BaseMdel
        '''

        my_model = BaseModel()
        my_model2 = BaseModel()

        # Checking that id attribute of type string
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model2.id), str)
        self.assertEqual(type(my_model.id), type(my_model2.id))

        # Checking that the two id are uniqe
        self.assertNotEqual(my_model.id, my_model2.id)

    def test_datetime(self):
        '''
        Test created_at and updated_at attribute
        '''

        my_model = BaseModel()
        current_date = datetime.now()

        current_date = current_date.strftime("%Y-%m-%dT%H:%M:%S")
        excepted_ouput = my_model.created_at.strftime("%Y-%m-%dT%H:%M:%S")
        self.assertEqual(excepted_ouput, current_date)

        # Check that created_at updated_at created at the same second
        excepted_created = my_model.created_at.strftime("%Y-%m-%dT%H:%M:%S")
        excepted_updated = my_model.updated_at.strftime("%Y-%m-%dT%H:%M:%S")
        self.assertEqual(excepted_created, excepted_updated)

        # Check the type of created_at and updated_at
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_init(self):
        '''
        Test for bassing arguments to class object
        '''

        my_model = BaseModel(name="My_First_Name", my_number=43)
        self.assertEqual(my_model.name, "My_First_Name")
        self.assertEqual(my_model.my_number, 43)
        self.assertEqual(type(my_model.name), str)
        self.assertEqual(type(my_model.my_number), int)

        my_mode2 = BaseModel()
        my_mode2.name = "My_First_Name"
        my_mode2.my_number = 43
        self.assertEqual(my_mode2.name, "My_First_Name")
        self.assertEqual(my_mode2.my_number, 43)
        self.assertEqual(type(my_mode2.name), str)
        self.assertEqual(type(my_mode2.my_number), int)

    def test_str(self):
        '''
        Test str method
        '''

        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        my_model2 = BaseModel()
        my_model2.name = "My First Model"
        my_model2.my_number = 89
        self.assertNotEqual(str(my_model), str(my_model2))
        self.assertNotEqual(my_model.id, my_model2.id)
        self.assertNotEqual(my_model.created_at, my_model2.created_at)
        self.assertNotEqual(my_model.updated_at, my_model2.updated_at)

        excepted_output = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(excepted_output, str(my_model))

    def test_save(self):
        '''
        Test save method
        '''

        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        # Check that updated_at attribute changed after using save method
        updated_at_before = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated_at_before, my_model.updated_at)
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

        # Checking for passing arguments to save method
        with self.assertRaises(TypeError) as msg:
            my_model.save("passing arguments")
        Err_msg = (
            "save() takes 1 positional argument but 2 were given"
            )
        self.assertEqual(Err_msg, str(msg.exception))

    def test_to_dict(self):
        '''
        Test to_dict method
        '''

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()
        my_model2 = BaseModel(**my_model_json)
        self.assertEqual(my_model.name, my_model2.name)
        self.assertEqual(my_model.my_number, my_model2.my_number)
        self.assertEqual(my_model.id, my_model2.id)
        self.assertEqual(str(my_model), str(my_model2))
        self.assertNotEqual(my_model, my_model2)
        self.assertIsInstance(my_model2, BaseModel)
        self.assertIsInstance(my_model_json, dict)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        datetime.strptime(str(my_model.created_at), '%Y-%m-%d %H:%M:%S.%f')
        datetime.strptime(str(my_model.updated_at), '%Y-%m-%d %H:%M:%S.%f')

        with self.assertRaises(TypeError) as msg:
            my_model_json = my_model.to_dict("Args")
        Err_msg = (
            "to_dict() takes 1 positional argument but 2 were given"
                   )
        self.assertEqual(Err_msg, str(msg.exception))


if __name__ == '__main__':
    unittest.main()
