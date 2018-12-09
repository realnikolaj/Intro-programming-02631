#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

def inputNumber(prompt):
    # INPUTNUMBER Prompts user to input a number
    #
    # Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
    # number. Repeats until user inputs a valid number.
    #
    # Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print("Not a number, please input a number from the menu")
            pass
    return num
