"""
Site: HackerRank
Type: Practice
Subdomain: Tutorials - 30 Days Of Code
Difficulty: Easy
Skill: Python 3
Problem: Day 3: Intro to Conditional Statements
URL: https://www.hackerrank.com/challenges/30-conditional-statements/problem
"""


# SOLUTION:

# v1 - Following the task description step-by-step:

def weirdometer(n):
    if n <= 0 or n > 100:  # Constraints: 1 <= n <= 100
        print('Out of range')
    elif n % 2 == 0 and 2 <= n <= 5:  # 'If n is even and in the inclusive range of 2 to 5, print "Not Weird"'
        print('Not Weird')
    elif n % 2 == 0 and 6 <= n <= 20:  # 'If n is even and in the inclusive range of 6 to 20, print "Weird"'
        print('Weird')
    elif n % 2 == 0 and n > 20:  # 'If n is even and greater than 20, print "Not Weird"'
        print('Not Weird')
    else:  # 'If n is odd, print "Weird"'
        print('Weird')


try:
    weirdometer(int(input('Input a number (1 to 100): ')))
except ValueError:
    print('This is not a number... you know that!!')


# v2 - Pythonic code:

def weirdometer(n):
    if n <= 0 or n > 100:
        print('Out of range')
    elif n % 2 == 1 or 5 < n < 21:
        print('Weird')
    else:
        print('Not Weird')


try:
    weirdometer(int(input('Input a number (1 to 100): ')))
except ValueError:
    print('This is not a number... you know that!!')

"""
NOTE:
More about "pythonic code":
https://stackoverflow.com/questions/25011078/what-does-pythonic-mean

Conditional Statements - Python Official Documentation (v3.9.1 PT-BR):
https://docs.python.org/pt-br/3/tutorial/controlflow.html
"""
