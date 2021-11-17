import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Frodo", 5.00)

    def test_customer_has_name(self):
        self.assertEqual("Frodo", self.customer.name)
    
    def test_customer_wallet_amount(self):
        result = self.customer.get_wallet_amount()
        self.assertEqual(5.00, result)