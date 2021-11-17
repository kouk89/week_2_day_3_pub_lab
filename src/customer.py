class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def get_wallet_amount(self):
        return self.wallet