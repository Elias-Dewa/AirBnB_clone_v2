#!/usr/bin/python3
"""Unittest for City"""
import os
import sys
from io import StringIO
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from datetime import datetime
import pep8


class TestCity(unittest.TestCase):
    """Test the city class"""

    def test_pep8(self):
        """Test for pep8 style"""
        pep8_style = pep8.StyleGuide(quiet=True)
        res = pep8_style.check_files(['models/city.py'])
        self.assertEqual(res.total_errors, 0, "errors found in console")

    def test_docstring(self):
        """Test for docstring"""
        set.assertIsNotNone(City.__doc__)

    def test_types_of(self):
        """Test for the types of attributes"""
        self.assertEqual(str, type(self.city.id))
        self.assertEqual(datetime, type(self.city.created_at))
        self.assertEqual(datetime, type(self.city.updated_at))

    def test_unique_id(self):
        """Test for unique id generation"""
        c = City()
        self.assertNotEqual(self.city.id, c.id)

    def test_instance(self):
        """Test for city is instance of City"""
        self.assertTrue(isinstance(self.city, City))

    def test_subclass(self):
        """Test for city is subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_str(self):
        """Test for __str__ method"""
        string = self.city.__str__()
        self.assertIn("[City] ({})".format(self.city.id), string)
        self.assertIn("'id': '{}'".format(self.city.id), string)
        self.assertIn("'created_at': {}".format(self.city.created_at), string)
        self.assertIn("'updated_at': {}".format(self.city.updated_at), string)

    def test_save(self):
        """Test for save method"""
        test = self.city.updated_at
        self.city.save()
        self.assertTrue(test != self.city.updated_at)

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertEqual(dict, type(self.city.to_dict))


if __name__ == '__main__':
    unittest.main()
