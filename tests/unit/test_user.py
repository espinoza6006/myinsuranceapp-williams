import unittest
from project.persistence.users_dao import *

class TestCustomer(unittest.TestCase):
    valid_user_id=1    
    invalid_user_id_1=None
    invalid_user_id_2=1000

    def test_get_user_products_valid(self):
        products = get_user_products(self.valid_user_id)
        # print(products)
        self.assertIsNotNone(products)
        self.assertTrue(len(products)>0)
    
    def test_get_user_products_invalid1(self):
        products = get_user_products(self.invalid_user_id_1)
        # print(products)
        self.assertTrue(len(products)==0)

    def test_get_user_products_invalid2(self):
        products = get_user_products(self.invalid_user_id_2)
        # print(products)
        self.assertTrue(len(products)==0)
