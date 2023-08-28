class CashRegister:
    def __init__(self, discount = 0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0
    
    def add_item(self, item_title, item_price, quantity = 1):
        item_price = float(item_price)
        self.total += item_price * quantity
        self.items.extend([item_title] * quantity)
        self.last_transaction = item_price * quantity
        
    def apply_discount(self):
        if self.discount > 0 :
            discount_amount = (self.discount / 100)* self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:2f}"
        else:
            return "There is no more discount to apply."   
          
    def void_last_transaction(self):
      if self.items:
        last_item_price = self.last_transaction / len(self.items)
        self.total -= last_item_price
        self.items.pop()
        self.last_transaction = last_item_price
      else:
        return "No transactions to void"  
 
      
                               