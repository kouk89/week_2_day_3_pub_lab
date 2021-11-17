import unittest 
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food_nachos = Food("Nachos", 3.00, 5)


    def test_food_has_name(self):
        self.assertEqual("Nachos", self.food_nachos.name)


    def test_food_has_price(self):
        self.assertEqual(3.00, self.food_nachos.price)
        
    def test_food_has_rejuvenation_level(self):
        self.assertEqual(5, self.food_nachos.rejuvenation_level)