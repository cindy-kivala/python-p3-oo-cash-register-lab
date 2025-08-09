#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total * (100 - self.discount) / 100
            total_display = int(self.total) if self.total.is_integer() else self.total
            print(f"After the discount, the total comes to ${total_display}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0
