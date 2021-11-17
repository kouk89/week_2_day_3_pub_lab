import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Frodo", 5.00, 18)
        self.drink = Drink("Beer", 2.50, 1)

    def test_customer_has_name(self):
        self.assertEqual("Frodo", self.customer.name)
    
    def test_customer_wallet_amount(self):
        result = self.customer.get_wallet_amount()
        self.assertEqual(5.00, result)
    
    def test_customer_has_age(self):
        result = self.customer.get_age()
        self.assertEqual(18, result)

    def test_get_customer_drunkenness(self):
        result = self.customer.get_drunkenness()
        self.assertEqual(0, result)

    def test_increase_drunkenness(self):
        self.customer.increase_drunkenness(self.drink)
        self.assertEqual(1, self.customer.drunkenness)

    