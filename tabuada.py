#!/usr/bin/env python
"""Exibe a tabuada de multiplicação de 1 a 10.

Ex:

Tabuada do 1:
1
2
3
...
-------------
Tabuada do 2:
2
4
6
...
--------------
"""
__version__ = '0.0.1'
__author__ = 'https://github.com/edsaantos/'
__license__ = 'Unlisence'

tabuada = list(range(1, 11))

for numeros in tabuada:
    print('Tabuada do', numeros,':')
    for numero in tabuada:
        print(numero * numeros)
    print('-' * 14)