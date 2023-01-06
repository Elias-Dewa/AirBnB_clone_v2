#!/usr/bin/python3
"""Unittest for review"""
import os
import sys
from io import StringIO
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime
import pep8


class TestReview(unittest.TestCase):
    """Test the review"""

    def test_pep8(self):
        """Test for pep8 style"""
        pep8_style = pep8.StyleGuide(quiet=True)
        res = pep8_style.check_files(['models/review.py'])
        self.assertEqual(res.total_errors, 0, "errors found in console")

    def test_docstring(self):
        """Test for docstring"""
        set.assertIsNotNone(Review.__doc__)

    def test_attribute(self):
        """Test for attribute"""
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)

    def test_types_of(self):
        """Test for the types of attributes"""
        self.assertEqual(str, type(self.review.text))
        self.assertEqual(str, type(self.review.user_id))
        self.assertEqual(str, type(self.review.place_id))

    def test_subclass(self):
        """Test for review is subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance(self):
        """Test for review is instance of review"""
        self.assertTrue(isinstance(self.review, Review))

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertEqual(dict, type(self.review.to_dict))

    def test_save(self):
        """Test for save method on review"""
        test = self.review.updated_at
        self.review.save()
        self.assertTrue(test != self.review.updated_at)


if __name__ == '__main__':
    unittest.main()
