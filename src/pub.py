

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def add_drink_to_drinks(self, drink):
        self.drinks.append(drink)

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink
    
    def check_overage(self, customer):
        return customer.get_age() >= 18
    
    def sell_drink(self, customer, drink_name):
        drink = self.find_drink_by_name(drink_name)
        if customer.wallet >= drink.price and drink in self.drinks and self.check_overage(customer):
            self.increase_till(drink.price)
            customer.decrease_wallet(drink.price)

        


