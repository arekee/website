from django.test import TestCase
from ..models import *

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to setup")
        pass
    def setUp(self):
        print("setUp:Run once for every")
        pass
    def test_arsen(self):
        print("Method: testfalseisfalse "        )
        self.assertFalse(False)
    def test_false_is_true(self):
        print("Method: testfalseistrue "        )
        self.assertTrue(True)
    def test_oneplusone(self):
        print("Method: oneplusone "        )
        postt=Posts()
        self.assertGreater(postt.myage(),15)
