# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:28:41 2018

"""

from random import randint
# dice value generator for 

face_value ={
            1:"Hit",
            2:"Vital",
            3:"Support",
            4:"Opportunity",
            5: "Shift",
            6: "Support-Vital",
            7: "Opportunity-Vital" }

def d4() :
    value = randint(1,4)
    try: 
        if value < 3:
            return face_value[1]
        elif value == 3:
            return face_value[4]
        elif value == 4:
            return face_value[5]
    except ValueError: 
        print("was not supplied an intiger")

def d8() :
    value = randint(1,8)
    try:
        if value < 5:
            return face_value[1]
        elif value == 5:
            return face_value[2]
        elif value == 6:
            return face_value[3]
        elif value == 7 :
            return face_value[5]
        elif value == 8:
            return face_value[4]
    except ValueError: 
        print("was not supplied an intiger")
        
        
def d12() :
    value = randint(1,12)
    try:
        if value < 5:
            return face_value[2]
        elif value > 4 & value < 8:
            return face_value[3]
        elif value >= 8 & value < 10:
            return face_value[4]
        elif value == 10:
            return face_value[1]
        elif value == 11:
            return face_value[6]
        elif value == 12:
            return face_value[7]
    except ValueError: 
        print("was not supplied an intiger")
        
def roller(Nofd4 = 0, Nofd8 = 0, Nofd12 = 0) :
        
        d4_values = [d4() for i in range(Nofd4)]
        d8_values = [d8() for i in range(Nofd8)]
        d12_values = [d12() for i in range(Nofd12)]
        
        print("d4 Results:")
        for result in d4_values:
            print(result)
        print ("d8 Results")
        for result in d8_values:
            print(result)
        print ("d12 results")
        for result in d12_values:
            print(result)
            

