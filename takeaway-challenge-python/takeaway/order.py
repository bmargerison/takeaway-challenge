from takeaway.takeaway import Takeaway

class Order():
    
    def __init__(self):
        self.basket = {}
        self.checkout_total = 0
        
    def add_to_basket(self, item, quantity):
        self.basket[item] = quantity
        
    def checkout(self):
        for k, v in self.basket.items():
            self.checkout_total += (Takeaway.menu[k] * v)
        print("Total to pay: %s" % self.checkout_total)