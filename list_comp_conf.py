# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:59:32 2018

@author: Nathan
"""

# list comp confusion 
from dice import d4

test = int(input("Positive Int Please :"))

x = [d4() for i in range(test)]

print (x)
