#!/usr/bin/python3
"""Unittest for base model"""
import os
import sys
from io import StringIO
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import pep8


class TestBaseModel(unittest.TestCase):
    """Test the base model"""

    def test_pep8(self):
        """Test for pep8 style"""
        pep8_style = pep8.StyleGuide(quiet=True)
        res = pep8_style.check_files(['models/base_model.py'])
        self.assertEqual(res.total_errors, 0, "errors found in console")

    def test_docstring(self):
        """Test for docstring"""
        set.assertIsNotNone(BaseModel.__doc__)
        set.assertIsNotNone(BaseModel.__init__.__doc__)
        set.assertIsNotNone(BaseModel.__str__.__doc__)
        set.assertIsNotNone(BaseModel.save.__doc__)
        set.assertIsNotNone(BaseModel.to_dic.__doc__)
        set.assertIsNotNone(BaseModel.delete.__doc__)

    def test_types_of(self):
        """Test for the types of attributes"""
        self.assertEqual(str, type(self.base.id))
        self.assertEqual(datetime, type(self.base.created_at))
        self.assertEqual(datetime, type(self.base.updated_at))

    def test_unique_id(self):
        """Test for unique id generation"""
        b = BaseModel()
        self.assertNotEqual(self.base.id, b.id)

    def test_instance(self):
        """Test for base is instance of BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_str(self):
        """Test for __str__ method"""
        string = self.base.__str__()
        self.assertIn("[BaseModel] ({})".format(self.base.id), string)
        self.assertIn("'id': '{}'".format(self.base.id), string)
        self.assertIn("'created_at': {}".format(self.base.created_at), string)
        self.assertIn("'updated_at': {}".format(self.base.updated_at), string)

    def test_save(self):
        """Test for save method"""
        test = self.base.updated_at
        self.base.save()
        self.assertTrue(test != self.base.updated_at)

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertEqual(dict, type(self.base.to_dict))

    def test_delete(self):
        """Test for delete method"""
        self.base.delete()
        self.assertNotIn(self.base, FileStorage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
