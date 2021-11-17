

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.foods = []

    def increase_till(self, amount):
        self.till += amount

    def add_drink_to_drinks(self, drink):
        self.drinks.append(drink)
    
    def add_food_to_foods(self, food):
        self.foods.append(food)

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink
    
    def find_food_by_name(self, food_name):
        for food in self.foods:
            if food.name == food_name:
                return food
    
    def check_overage(self, customer):
        return customer.get_age() >= 18
    
    def sell_drink(self, customer, drink_name):
        drink = self.find_drink_by_name(drink_name)
        drunkenness = customer.get_drunkenness()
        if drunkenness < 10:
            if drink in self.drinks:
                if customer.wallet >= drink.price:
                    if self.check_overage(customer):
                        self.increase_till(drink.price)
                        customer.decrease_wallet(drink.price)
                        customer.increase_drunkenness(drink)

        


