import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_beer = Drink("Beer", 2.50)
        self.drink_wine = Drink("Wine", 1.50)
        self.drink_spirit = Drink("Spirit", 2.00)

    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink_beer.name)
    
    def test_drink_has_price(self):
        self.assertEqual(2.50,self.drink_beer.price)