# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:11:05 2018

"""   
    # TO DO
    # Do some input cleanseing 
    # Get a python shell that isnt anaconda
    # Learn how to make a GUI
    # print the sprites for the required value in a GUI
    

import pw_dice as dice


def main() :       
    roll_more = 1
    while roll_more = 1 :
        # lets get some user input
        x = input("What dice are you rolling? Format Nofd4,Nofd8,Nofd12 :")
        x = x.split(',')
        
        d4 = int(x[0])
        d8 = int(x[1])
        d12 = int(x[2])
         
    dice.roller(d4,d8,d12)
    
    x = input 
    
main()
