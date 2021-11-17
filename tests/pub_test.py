import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Frodo", 5.00, 18)
        self.customer_new = Customer("Sam", 1.00, 18)
        self.customer_underage = Customer("Pippin", 5.00, 17)
        self.drink_beer = Drink("Beer", 2.50, 1)
        self.drink_strong = Drink("Zombie", 1.00, 5)
        self.food_nachos = Food("Nachos", 2.00, 3)
        

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

    def test_sell_drink__sufficient_funds(self):
        self.pub.add_drink_to_drinks(self.drink_beer)
        self.pub.sell_drink(self.customer, "Beer")
        self.assertEqual(102.50, self.pub.till)
        self.assertEqual(2.50, self.customer.wallet)
    
    def test_sell_drink__insufficient_funds(self):
        self.pub.add_drink_to_drinks(self.drink_beer)
        self.pub.sell_drink(self.customer_new, "Beer")
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(1.00, self.customer_new.wallet)
    
    def test_check_age__underage(self):
        result = self.pub.check_overage(self.customer_underage)
        self.assertEqual(False, result)
    
    def test_sell_drink__underage(self):
        self.pub.add_drink_to_drinks(self.drink_beer)
        self.pub.sell_drink(self.customer_underage, "Beer")
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(5.00, self.customer_underage.wallet)

    def test_sell_drink__too_drunk(self):
        self.pub.add_drink_to_drinks(self.drink_strong)
        self.pub.sell_drink(self.customer, "Zombie")
        self.pub.sell_drink(self.customer, "Zombie")
        self.pub.sell_drink(self.customer, "Zombie")
        self.assertEqual(102.00, self.pub.till)
        self.assertEqual(3.00, self.customer.wallet)
        self.assertEqual(10, self.customer.drunkenness)

    def test_pub_foods_initialised_empty(self):
        self.assertEqual(0, len(self.pub.foods))
    
    def test_add_food_to_foods(self):
        self.pub.add_food_to_foods(self.food_nachos)
        self.assertEqual(1, len(self.pub.foods))
    
    def test_find_food_by_name(self):
        self.pub.add_food_to_foods(self.food_nachos)
        result = self.pub.find_food_by_name("Nachos")
        self.assertEqual("Nachos", result.name)
    
    def test_sell_food__sufficient_funds(self):
        self.pub.add_food_to_foods(self.food_nachos)
        self.pub.add_drink_to_drinks(self.drink_strong)
        self.pub.sell_drink(self.customer, "Zombie")
        self.pub.sell_food(self.customer, "Nachos")
        self.assertEqual(103.00, self.pub.till)
        self.assertEqual(2, self.customer.drunkenness )
        self.assertEqual(2, self.customer.wallet)
    
    def test_initialise_stock(self):
        self.pub.add_drink_to_drinks(self.drink_strong)
        self.assertEqual(1, self.pub.stock["Zombie"])
    
    def test_sell_drink__reduce_stock(self):
        self.pub.add_drink_to_drinks(self.drink_strong)
        self.pub.sell_drink(self.customer, "Zombie")
        self.assertEqual(0, self.pub.stock["Zombie"])


        



    