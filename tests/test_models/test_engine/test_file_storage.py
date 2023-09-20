#!/usr/bin/python3
""" Module for testing file storage"""
import json
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from os import path
import pep8
import unittest


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_FileStorage(unittest.TestCase):
    """Test the FileStorage"""
    def test_docstring(self):
        """module docstring length"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_FileStorage_arg(self):
        """testing file storage with an argument"""
        with self.assertRaises(TypeError):
            FileStorage("Holberton")
        with self.assertRaises(TypeError):
            FileStorage("89")
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_is_an_instance(self):
        """function test_is_an_instance"""
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)

    def test_storage(self):
        """testing storage"""
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage), FileStorage)

    def test_file_path(self):
        """testing file path"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_All(self):
        """Test the FileStorage method itself using example """
        object_1 = FileStorage()
        object_data = object_1.all()
        self.assertIsNotNone(object_data)
        self.assertEqual(type(object_data), dict)

    def test_FileStorage_1(self):
        """Tests the FileStorage again"""
        my_model = FileStorage()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(str(type(FileStorage)), "<class 'type'>")
        self.assertTrue(isinstance(my_model, FileStorage))
        self.assertTrue(type(my_model), object)
    
    def test_reload(self):
        """tests the reload"""
        if not path.exists("file.json"):
            new_file = FileStorage()
            new_base = BaseModel(id="123", created_at="2021-02-17T22:46:38.86",
                                 updated_at="2021-02-17T22:46:38.86")
            new_city = City()
            new_file.new(new_base)
            new_file.new(new_city)
            new_file.save()
        with open("file.json", "r") as f:
            obj = json.load(f)
        self.assertEqual(type(obj), dict)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_save(self):
        '''Test save method'''
        objs = storage
        new_base = BaseModel()
        new_user = User()
        new_state = State()
        new_place = Place()
        new_city = City()
        new_amenity = Amenity()
        new_review = Review()
        objs.new(new_base)
        objs.new(new_user)
        objs.new(new_state)
        objs.new(new_place)
        objs.new(new_city)
        objs.new(new_amenity)
        objs.new(new_review)
        objs.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + new_base.id, save_text)
            self.assertIn("User." + new_user.id, save_text)
            self.assertIn("State." + new_state.id, save_text)
            self.assertIn("Place." + new_place.id, save_text)
            self.assertIn("City." + new_city.id, save_text)
            self.assertIn("Amenity." + new_amenity.id, save_text)
            self.assertIn("Review." + new_review.id, save_text)

    def test_new(self):
        '''Test new method'''
        new_file = FileStorage()
        new_base = BaseModel(id="123", created_at="2021-02-17T22:46:38.883036",
                             updated_at="2021-02-17T22:46:38.883036")
        new_city = City()
        new_amenity = Amenity()
        new_user = User()
        new_place = Place()
        new_review = Review()
        new_state = State()
        new_file.new(new_base)
        new_file.new(new_city)
        new_file.new(new_amenity)
        new_file.new(new_place)
        new_file.new(new_state)
        new_file.new(new_user)
        new_file.new(new_review)
        objs = new_file.all()
        key = new_base.__class__.__name__ + "." + new_base.__dict__["id"]
        key_2 = new_city.__class__.__name__ + "." + new_city.__dict__["id"]
        key_user = new_user.__class__.__name__ + "." + new_user.__dict__["id"]
        key_review = new_review.__class__.__name__ + "." + new_review.__dict__["id"]
        key_place = new_place.__class__.__name__ + "." + new_place.__dict__["id"]
        key_state = new_state.__class__.__name__ + "." + new_state.__dict__["id"]
        key_amenity = new_amenity.__class__.__name__ + "." + new_amenity.__dict__["id"]
        self.assertIn(key, objs)
        self.assertIn(key_2, objs)
        self.assertIn(key_user, objs)
        self.assertIn(key_review, objs)
        self.assertIn(key_place, objs)
        self.assertIn(key_state, objs)
        self.assertIn(key_amenity, objs)

if __name__ == '__main__':
    unittest.main()
