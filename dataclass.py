# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:32:32 2021

@author: senol.isci
"""
class MyVar: 
    # Defining __init__ method
    def __init__(self,text=None):
        self.ver=text
    def show(self):
        print(self.ver)
      

       
from dataclasses import dataclass

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: MyVar()
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    def mello(self) -> float:
        print(5)
        return 5