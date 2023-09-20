#!/usr/bin/python3
""" file that tests the City class"""
from models.base_model import BaseModel
from models.city import City
import pep8
import inspect
import unittest


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDocs(unittest.TestCase):
    """Base model document tests"""

    @classmethod
    def setUpClass(cls):
        """Testing class"""
        cls.city_funcs = inspect.getmembers(City, inspect.isfunction)

    def test_module_docstring(self):
        """module docstring length"""
        self.assertTrue(len(City.__doc__) >= 1)

    def test_class_docstring(self):
        """Class docstring length"""
        self.assertTrue(len(City.__doc__) >= 1)


class test_City(BaseModel):
    """ tests the City class """

    def __init__(self, *args, **kwargs):
        """ initialization """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ tests the state id """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ test the name """
        new = self.value()
        self.assertEqual(type(new.name), str)
