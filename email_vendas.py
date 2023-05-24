#!/usr/bin/env python
'''
Este código envia um email marketing para clientes atribuidos na env

    client_list = ['Maria', 'Joao', 'Daniele']

    com as informações inseridas no dicionário abaixo
     
    print(email_tmpl % {
        'name': client,
        'product': 'Ração DogDream 1kg',
        'product_description': 'Alimentar seu animal de estimação.',
        'product_url': 'https://dogshop.com',
        'product_amount': 8,
        'product_value': 59.90
    })
'''
__version__ = '0.0.1'
__author__ = 'https://github.com/edsaantos/'
__license__ = 'Unlicense'

client_list = ['Maria', 'Joao', 'Daniele']
email_tmpl = '''Olá, %(name)s.

Temos uma promocao imperdível para o produto %(product)s!

Ele é um ótimo produto para:
%(product_description)s

Clique no link %(product_url)s para garantir sua unidade.

Restam apenas %(product_amount)d disponíveis!

O preco promocional é de %(product_value).2f dinheiros.
'''

for client in client_list:
    print(email_tmpl % {
        'name': client,
        'product': 'Ração DogDream 1kg',
        'product_description': 'Alimentar seu animal de estimação.',
        'product_url': 'https://dogshop.com',
        'product_amount': 8,
        'product_value': 59.90
    })