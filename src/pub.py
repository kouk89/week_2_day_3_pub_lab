

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.foods = []
        self.stock = {}

    def increase_till(self, amount):
        self.till += amount

    def add_drink_to_drinks(self, drink):
        self.drinks.append(drink)
        if not drink.name in self.stock:
            self.stock[drink.name] = 1
    
    def increase_stock(self, amount, drink):
        self.stock[drink.name] += amount
    
    def decrease_stock(self, amount, drink):
        self.stock[drink.name] -= amount

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
                        self.decrease_stock(1, drink)
    
    def sell_food(self, customer, food_name):
        food = self.find_food_by_name(food_name)
        if food in self.foods and customer.wallet >= food.price:
            self.increase_till(food.price)
            customer.decrease_wallet(food.price)
            customer.decrease_drunkenness(food)
            

        


