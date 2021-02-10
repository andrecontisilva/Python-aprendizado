"""
Site: HackerRank
Type: Practice
Subdomain: Tutorials - 30 Days Of Code
Difficulty: Easy
Skill: Python 3
Problem: Day 2: Operators
URL: https://www.hackerrank.com/challenges/30-operators/problem
"""


# SOLUTION:

# v1 - Simple solution for HackerRank Console:


# #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    total = round(meal_cost + tax + tip)
    print(total)


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)


# v2 - The v1 code with more details:

# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    print(f"Tip: {tip}")  # Print the tip value.
    tax = meal_cost * (tax_percent / 100)
    print(f"Tax: {tax}")  # Print the tax value.
    total = round(meal_cost + tax + tip)
    print(f"The total cost of your meal is ${total}.")


if __name__ == '__main__':
    meal_cost = float(input("Input the meal cost: "))

    tip_percent = int(input("Input the tip percent: "))

    tax_percent = int(input("Input the tax percent: "))

    solve(meal_cost, tip_percent, tax_percent)

"""
NOTE:
Operators - Python Official Documentation (v3.9.1 PT-BR):
https://docs.python.org/pt-br/3/tutorial/introduction.html
"""
