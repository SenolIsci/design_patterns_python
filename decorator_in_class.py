# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:07:41 2021

@author: senol.isci
"""




class A():
    def __init__(self,number=0):
        self.num=number
        self.connection=True
        
    def decorator(func):

        def wrapper_decorator(self,*args,**argv):
            # Do something before
            if self.connection:
                value = func(self,*args,**argv)
                # Do something after
                if args[0] % 2 == 0:
                    return value*100
                else:
                    return value
            else:
                return None
        return wrapper_decorator


    @decorator
    def inc(self,no):
        self.num=self.num+no
        return self.num

a=A()
print(a.inc(3))
print(a.inc(6))

