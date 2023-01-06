#!/usr/bin/python3
"""Unittest for amenity"""
import os
import sys
from io import StringIO
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
import pep8


class TestAmenity(unittest.TestCase):
    """Test the amenity"""

    def test_pep8(self):
        """Test for pep8 style"""
        pep8_style = pep8.StyleGuide(quiet=True)
        res = pep8_style.check_files(['models/amenity.py'])
        self.assertEqual(res.total_errors, 0, "errors found in console")

    def test_docstring(self):
        """Test for docstring"""
        set.assertIsNotNone(Amenity.__doc__)

    def test_attribute(self):
        """Test for attribute"""
        self.assertTrue('name' in self.amenity.__dict__)
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)

    def test_types_of(self):
        """Test for the types of attributes"""
        self.assertEqual(str, type(self.amenity.name))
        self.assertEqual(datetime, type(self.amenity.created_at))
        self.assertEqual(datetime, type(self.amenity.updated_at))

    def test_unique_id(self):
        """Test for unique id generation"""
        a = Amenity()
        self.assertNotEqual(self.amenity.id, a.id)

    def test_subclass(self):
        """Test for amenity is subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance(self):
        """Test for amenity is instance of Amenity"""
        self.assertTrue(isinstance(self.amenity, Amenity))

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertEqual(dict, type(self.base.to_dict))

    def test_save(self):
        """Test for save method on Amenity"""
        test = self.amenity.updated_at
        self.amenity.save()
        self.assertTrue(test != self.amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
