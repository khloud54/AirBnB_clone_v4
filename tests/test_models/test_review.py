#!/usr/bin/python3
"""
Module for the Review class.
"""
import models.review import Review
import unittest


class TestUser(unittest.TestCase):
    """
    Review class Unittest
    """

    def test_object_Instantiation(self):
        """
        instantiates class
        """
        self.review = Review()

    def testattr(self):
        ''' Test the attributes of the Review class '''
        self.review = Review()
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertFalse(hasattr(self.review, "random_attr"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertEqual(self.review.text, "")
        self.assertEqual(self.review.__class__.__name__, "Review")

    def testsave(self):
        ''' testing method: save '''
        self.review = Review()
        self.review.save()
        self.assertTrue(hasattr(self.review, "updated_at"))

    def teststr(self):
        ''' testing __str__ return format of BaseMode '''
        self.review = Review()
        s = "[{}] ({}) {}".format(self.review.__class__.__name__,
                                  str(self.review.id), self.review.__dict__)
        self.assertEqual(print(s), print(self.review))

if __name__ == '__main__':
        unittest.main()
