class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
    
    def get_wallet_amount(self):
        return self.wallet
    
    def decrease_wallet(self,amount):
        self.wallet -= amount
    
    def get_age(self):
        return self.age