#!/usr/bin/python3
"""Unittest for place"""
import os
import sys
from io import StringIO
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
import pep8


class TestPlace(unittest.TestCase):
    """Test the place"""

    def test_pep8(self):
        """Test for pep8 style"""
        pep8_style = pep8.StyleGuide(quiet=True)
        res = pep8_style.check_files(['models/place.py'])
        self.assertEqual(res.total_errors, 0, "errors found in console")

    def test_docstring(self):
        """Test for docstring"""
        set.assertIsNotNone(Place.__doc__)

    def test_attribute(self):
        """Test for attribute"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)

    def test_types_of(self):
        """Test for the types of attributes"""
        self.assertEqual(str, type(self.place.name))
        self.assertEqual(str, type(self.place.city_id))
        self.assertEqual(str, type(self.place.user_id))
        self.assertEqual(str, type(self.place.description))
        self.assertEqual(int, type(self.place.number_rooms))
        self.assertEqual(int, type(self.place.number_bathrooms))
        self.assertEqual(int, type(self.place.max_guest))
        self.assertEqual(int, type(self.place.price_by_night))
        self.assertEqual(int, type(float.place.latitude))
        self.assertEqual(int, type(float.place.longitude))

    def test_subclass(self):
        """Test for place is subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance(self):
        """Test for place is instance of place"""
        self.assertTrue(isinstance(self.place, Place))

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertEqual(dict, type(self.place.to_dict))

    def test_save(self):
        """Test for save method on place"""
        test = self.place.updated_at
        self.place.save()
        self.assertTrue(test != self.place.updated_at)


if __name__ == '__main__':
    unittest.main()
