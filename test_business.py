import unittest

from business import Business 

class BusinessTestCase(unittest.TestCase):

    def setUp(self):
        self.bus = Business()

    def test_create_business(self):
        response = bus.create_business("Andela", "Trm")
        self.assertEqual("message": "Business added succesfully")

    def test_cannot_dublicate_business(self):
        pass
