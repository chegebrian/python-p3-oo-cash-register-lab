#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0, items=None):
        self.discount = discount
        self.total = total
        self.items = items if items is not None else []
        self.last_transaction = None  # Tracks last add_item call

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = {"title": title,
                                 "price": price, "quantity": quantity}
        return self.total

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total -= (self.total * (self.discount/100))
            print(f"After the discount, the total comes to ${self.total:.0f}.")
            return self.total

    def void_last_transaction(self):
        if self.last_transaction:
            # Subtract total of last transaction
            self.total -= self.last_transaction["price"] * \
                self.last_transaction["quantity"]
            # Remove last items from the items list
            for _ in range(self.last_transaction["quantity"]):
                self.items.pop()
            # Reset last transaction
            self.last_transaction = None
