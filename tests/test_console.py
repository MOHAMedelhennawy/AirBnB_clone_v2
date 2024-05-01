#!/usr/bin/python3
"""
Modeule to test console functionality
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import uuid
from models.engine.file_storage import FileStorage
from models.state import State
from models.place import Place

class TestHBNBCommand(unittest.TestCase):
    """
    Unit tests for HBNBC command interpreter
    """

    def test_create(self):
        """
        Test create function in console
        """
        with patch('sys.stdout', new=StringIO()) as output:
            input = "create"
            expected_out = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "create MyModel"
            expected_out = "** class doesn't exist **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "create BaseModel"
            HBNBCommand().onecmd(input)
            out = output.getvalue().strip()
            self.assertTrue(uuid.UUID(out, version=4))

        with patch('sys.stdout', new=StringIO()) as output:
            input = "create User"
            HBNBCommand().onecmd(input)
            out = output.getvalue().strip()
            self.assertTrue(uuid.UUID(out, version=4))

        with patch('sys.stdout', new=StringIO()) as output:
            input = "create State"
            HBNBCommand().onecmd(input)
            out = output.getvalue().strip()
            self.assertTrue(uuid.UUID(out, version=4))

        with patch('sys.stdout', new=StringIO()) as output:
            input = "create City"
            HBNBCommand().onecmd(input)
            out = output.getvalue().strip()
            self.assertTrue(uuid.UUID(out, version=4))

        with patch('sys.stdout', new=StringIO()) as output:
            input = "create Amenity"
            HBNBCommand().onecmd(input)
            out = output.getvalue().strip()
            self.assertTrue(uuid.UUID(out, version=4))

        with patch('sys.stdout', new=StringIO()) as output:
            input = "create Place"
            HBNBCommand().onecmd(input)
            out = output.getvalue().strip()
            self.assertTrue(uuid.UUID(out, version=4))

        with patch('sys.stdout', new=StringIO()) as output:
            input = "create Review"
            HBNBCommand().onecmd(input)
            out = output.getvalue().strip()
            self.assertTrue(uuid.UUID(out, version=4))

        with patch('sys.stdout', new=StringIO()) as output:
            input = 'create State name="California"'
            HBNBCommand().onecmd(input)
            output_id = output.getvalue().strip() # id
            self.assertTrue(uuid.UUID(output_id, version=4))
            
            state = FileStorage.all(State)["State." + output_id]
            self.assertEqual(output_id, state.id)
            self.assertEqual(state.name, "California")
            self.assertTrue(state.created_at)
            self.assertTrue(state.updated_at)
            self.assertIsInstance(state, State)

        with patch('sys.stdout', new=StringIO()) as output:
            input = 'create Place city_id="0001" user_id="0001" name="My_little_house" \
                     number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 \
                     latitude=37.773972 longitude=-122.431297'
            
            HBNBCommand().onecmd(input)
            output_id = output.getvalue().strip() # id
            self.assertTrue(uuid.UUID(output_id, version=4))

            place = FileStorage.all(Place)["Place." +  output_id]
            self.assertIsInstance(place, Place)
            self.assertEqual(place.id, output_id)
            self.assertEqual(place.name, 'My little house')
            self.assertIsInstance(place.name, str)
            self.assertEqual(place.number_rooms, 4)
            self.assertIsInstance(place.number_rooms, int)
            self.assertEqual(place.number_bathrooms, 2)
            self.assertIsInstance(place.number_bathrooms, int)
            self.assertEqual(place.max_guest, 10)
            self.assertIsInstance(place.max_guest, int)
            self.assertEqual(place.price_by_night, 300)
            self.assertIsInstance(place.price_by_night, int)
            self.assertEqual(place.city_id, "0001")
            self.assertIsInstance(place.city_id, str)
            self.assertEqual(place.user_id, "0001")
            self.assertIsInstance(place.user_id, str)
            self.assertEqual(place.latitude, 37.773972)
            self.assertIsInstance(place.latitude, float)
            self.assertEqual(place.longitude, -122.431297)
            self.assertIsInstance(place.longitude, float)




    def test_show(self):
        """
        Test show function in console
        """
        with patch('sys.stdout', new=StringIO()) as output:
            input = "show"
            expected_out = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show MyModel"
            expected_out = "** class doesn't exist **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show BaseModel"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show State"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show City"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show Amenity"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show Place"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show Review"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show BaseModel 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show User 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show State 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show City 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show Place 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show Review 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "show Amenity 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

    def test_destroy(self):
        """
        Test destroy function in console
        """
        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy"
            expected_out = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy MyModel"
            expected_out = "** class doesn't exist **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy BaseModel"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy State"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy City"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy Amenity"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy Place"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy Review"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy BaseModel 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy User 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy State 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy City 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy Place 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy Review 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "destroy Amenity 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

    def test_all(self):
        """
        Test all function in console
        """
        with patch('sys.stdout', new=StringIO()) as output:
            input = "all MyModel"
            expected_out = "** class doesn't exist **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

    def test_update(self):
        """
        Test update function in console
        """
        with patch('sys.stdout', new=StringIO()) as output:
            input = "update"
            expected_out = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update MyModel"
            expected_out = "** class doesn't exist **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update BaseModel"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update State"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update City"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update Amenity"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update Place"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update Review"
            expected_out = "** instance id missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update BaseModel 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update User 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update State 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update City 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update Place 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update Review 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            input = "update Amenity 1212"
            expected_out = "** no instance found **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected_out, output.getvalue().strip())
