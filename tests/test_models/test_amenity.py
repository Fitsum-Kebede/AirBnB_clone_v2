#!/usr/bin/python3
""" amenity test file """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8
import inspect


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDocs(unittest.TestCase):
    """Base model document tests"""

    @classmethod
    def setUpClass(cls):
        """Testing class"""
        cls.amenity_funcs = inspect.getmembers(Amenity, inspect.isfunction)

    def test_module_docstring(self):
        """module docstring length"""
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_class_docstring(self):
        """Class docstring length"""
        self.assertTrue(len(Amenity.__doc__) >= 1)


class test_Amenity(BaseModel):
    """ class that test the Amenity class """

    def __init__(self, *args, **kwargs):
        """ idk """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ idk """
        new = self.value()
        self.assertEqual(type(new.name), str)
