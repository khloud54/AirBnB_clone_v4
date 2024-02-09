#!/usr/bin/python3
"""
Module for BaseModel unitest
"""
import unittest
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    ''' BaseModel class unittest '''

    def test_object_Instantiation(self):
        ''' Creates an instance of the class '''
        self.basemodel = BaseModel()

    def testattr(self):
        ''' Test the attributes of the User class '''
        self.basemodel = BaseModel()
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "updated_at"))
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.assertFalse(hasattr(self.basemdel, "name"))
        self.assertFalse(hasattr(self.basemdel, "random_attr"))
        self.basemodel.name = "Alice"
        self.basemodel.age = "44"
        self.assertTrue(hasattr(self.basemodel, "name"))
        self.assertTrue(hasattr(self.basemodel, "age"))
        delattr(self.basemodel, "name")
        self.assertFalse(hasattr(self.basemdel, "name"))
        delattr(self.basemodel, "age")
        self.assertFalse(hasattr(sel.basemodel, "age"))
        self.assertEqual(self.basemodel.__class__.__name__, "BaseModel")

    def test_checking_for_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_to_dict(self):
        base1 = BaseModel()
        base1_dict = base1.to_dict()
        self.assertEqual(base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'],str)

    def testsave(self):
        ''' save testing method '''
        self.basemodel = BaseModel()
        self.basemodel.save()
        self.assertTrue(hasattr(self.basemodel, "updated_at"))

    def teststr(self):
        ''' testing __str__ return format of BaseModel '''
        self.basemodel = BaseModel()
        s = "[{}] ({}) {}".format(self.basemodel.__class.__name__,
                                  str(self.basemodel.id),
                                  self.basemodel.__dict__)
        self.assertEqual(print(s), print(self.basemodel))


    if __name__ == '__main__':
        unittest.main()
