#!/usr/bin/env python3
"""Display Multiplication Table for numbers 1 to 10.

Ex:

---Multiplication Table for 1---
    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
...
############################################################
---Multiplication Table for 2---
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
...
############################################################
"""
__version__ = '0.1.1'
__author__ = 'https://github.com/edsaantos/'
__license__ = 'Unlisence'

table = list(range(1, 11))

for number_one in table:
    print('{:^80}'.format(f'---Multiplication Table for {number_one}---\n'))
    for number_two in table:
        result = number_one * number_two
        print('{:^80}'.format(f'{number_one} x {number_two} = {result}'), '\n')
    print('{:^80}'.format('#' * 60), '\n')