#!/usr/bin/python3
import sys
from datetime import datetime


class PointOfSale:
    """Creates and computes cost in a shop"""

    def __init__(self, name='', item=0, quantity=0, price=0):
        self.name = name
        self.item = item
        self.quantity = quantity
        self. price = price
        self.date = datetime.now()

    def __str__(self):
        return str(tuple(getattr(self.i) for i in self.__dict__))


def provide_details():
    # while True:
    #     name = input("Name: ")
    #     item = input("item: ")
    #     quantity = int(input("Quantity: "))
    #     price = int(input("price: "))

    shop = PointOfSale()

    print(shop)
    print(sys.argv)

provide_details()