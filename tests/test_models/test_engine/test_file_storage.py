#!/usr/bin/python3
""""
Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.engine import file_storage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestClass):
   """
   unittests for testing FileStorage

   """

   def test_Instatiation(self):
       ''' checks instance of class BaseModel '''
       obj = FileStorage()
       self.assertIsInstance(obj, FileStorage)

    def test_Access(self):
        ''' test read-write acess permissions '''
        read = os.access('models/engine/file_storage.py', os.R_Ok)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_Ok)
        self.assertTrue(write)
        execute = os.access('models/engine/file_storage.py', os.X_Ok)
        self.assertFalse(execute)

    def test_new(self):
        """
        Tests method: new (saves new object into dictionary)
        """
       m_storage = FileStorage()
       instances_dic = m_storage.all()
       Aman = User()
       Aman.id = 999999
       Aman.name = "Amab"
       m_storage.new(Aman)
       key = Aman.__class__.name__ + "." + str(Aman.id)
       self.assertIsNotNone(instances_dic[key])

    def test_reload(self):
        """
        Tests method: reloaf objects from string file
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            content = r.read() # Read the whole file content
            self.assertEqual(content, "{}")
        self.assertIsNone(a_storage.reload())

    def test_funcdocs(self):
        ''' functions docstring testing '''
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)

    def test_save(self):
        ''' method of test save '''
        storage = FileStorage()
        new_obj = BaseModel()
        storage.new(new_obj)
        dict_a = storage.all()
        storage.save()
        storage.reload()
        dict_b = storage.all()
        key_a = next(iter(dict_a))
        key_b = next(iter(dict_b))
        self.assertEqual(dict_a[key_a].to_dict(), dict_b[key_b].to_dict())

    if __name__ == '__main__':
        unittest.main()

