# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:30:20 2021

@author: senol.isci
"""
# Defining class


class MyCar: 
    # Defining __init__ method
    def __init__(self,text=None):
        self.ver=text
    def show(self):
        print(self.ver)

from dataclasses import dataclass

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=True, frozen=False)
        
# Defining class
class Portal:
    __name :int=5
    idc:int=10
    ff:object=print
  
      
    # Using @property decorator
    @property
    # Getter method
    def name(self):
        return self.__name
      
    # Setter method
    @name.setter
    def name(self, val):
        self.__name = val
  
    # Deleter method
    @name.deleter
    def name(self):
       del self.__name
       
        
    def double_id_noprop(self):
        return MyCar("")
     
    @property
    def double_id(self):
        print("hello")
        return MyCar("")

    @property
    def update_profile(self):
        return bind_api(string="msmsms")
        
    
    def update_profile_noprop(self):
        return bind_api(string="msmsms")




def bind_api(**config):
    
    class MyVar: 
        cstring=config["string"]
        # Defining __init__ method
        def __init__(self,text):
            self.ver=text+self.cstring
        def show(self):
            print(self.ver)
      
    
    def _call(*args,**kwargs):
        print("kwargs myind",kwargs["myind"])
        a=MyVar("ooo ")
        print("call")
        return a.ver
   
    return _call


p=Portal("hello")

print(p.update_profile(myind=23412342))

#print(p.update_profile_noprop()(myind=23412342))

print(p.name)