# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:11:05 2018

@author: Nathan
"""   
    # TO DO
    # Find the number of dice and their size to roll
    # Generate a random number from 1 - x
    # Compare output with dice symbols
    # print the sprites for the required value

import pw_dice as dice


def main() :       
    
    # lets get some user input
    x = input("What dice are you rolling? Format Nofd4,Nofd8,Nofd12 :")
    x = x.split(',')
        
    d4 = int(x[0])
    d8 = int(x[1])
    d12 = int(x[2])
         
    dice.roller(d4,d8,d12)
    
main()