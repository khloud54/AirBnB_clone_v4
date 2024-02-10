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
        rd = os.access('models/engine/file_storage.py', os.R_Ok)
        self.assertTrue(read)
        wr = os.access('models/engine/file_storage.py', os.W_Ok)
        self.assertTrue(write)
        ex = os.access('models/engine/file_storage.py', os.X_Ok)
        self.assertFalse(ex)

    def test_new(self):
        """
        Test the new method, which stores a new object in a dictionary
        """
       m_storage = FileStorage()
       instances_dic = m_storage.all()
       Aman = User()
       Aman.id = 999999
       Aman.name = "Aman"
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
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
            self.assertIs(a_storage.reload(), None)

    def test_funcdocs(self):
        ''' functions docstring testing '''
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)

    def test_save(self):
        ''' method of test save '''
        obj = FileStorage()
        new_obj = BaseModel()
        obj.new(new_obj)
        dict1 = obj.all()
        obj.save()
        obj.reload()
        dict2 = obj.all()
        for key in dict1:
            key1 = key
        for key in dict2:
            key2 = key
        self.assertEqual(dict1[key].to_dict(), dict2[key2].to_dict())

if __name__ == '__main__':
    unittest.main()
