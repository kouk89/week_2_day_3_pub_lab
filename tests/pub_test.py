import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Frodo", 5.00)
        self.drink_beer = Drink("Beer", 2.50)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
      
    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.5, self.pub.till)

    def test_pub_drinks_list_initialised_empty(self):
        self.assertEqual(0, len(self.pub.drinks))

    def test_add_drink_to_drinks(self):
        self.pub.add_drink_to_drinks(self.drink_beer)
        self.assertEqual(1, len(self.pub.drinks))

    def test_find_drink_by_name(self):
        self.pub.add_drink_to_drinks(self.drink_beer)
        result = self.pub.find_drink_by_name("Beer")
        self.assertEqual("Beer", result.name)

    def test_sell_drink(self):
        self.pub.add_drink_to_drinks(self.drink_beer)
        self.pub.sell_drink(self.customer, "Beer")
        self.assertEqual(102.50, self.pub.till)
        self.assertEqual(2.50, self.customer.wallet)

        



    