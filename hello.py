#!/usr/bin/env python3
"""Hello World multi language.
Depending on the language set in the environment, the program
displays the corresponding message.

How to use:

Make sure the LANG variable is properly configured,
check the variable with 'env' or create the variable with 'export':

    env | grep LANG
    ou
    export LANG=pt_BR.UTF-8

Execution:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = '0.0.1'
__author__ = 'https://github.com/edsaantos/'
__license__ = 'Unlicense'

import os

current_language = os.getenv('LANG', 'en_US.utf8')[:5]
message = 'Hello, World!'

if current_language == 'pt_BR':
    message = 'Olá, Mundo!'
elif current_language == 'it_IT':
    message = 'Ciao, Mondo!'
elif current_language == 'fr_FR':
    message = 'Bonjour, le monde'
elif current_language == 'es_SP':
    message = 'Hola, Mondo'

print(message)