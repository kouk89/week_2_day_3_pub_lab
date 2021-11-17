class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0
    
    def get_wallet_amount(self):
        return self.wallet
    
    def decrease_wallet(self,amount):
        self.wallet -= amount
    
    def get_age(self):
        return self.age

    def get_drunkenness(self):
        return self.drunkenness

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level
    
    def decrease_drunkenness(self,food):
        self.drunkenness -= food.rejuvenation_level
        