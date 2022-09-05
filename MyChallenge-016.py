# Criar um Programa que leia um "NÚMERO REAL" qualquer pelo Teclado
# e mostre na Tela a sua porção "INTEIRA"

from math import ceil, floor, trunc

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 016: ***')

print()

nome = input('Whats your Name? ')

print()

num = float(input('Type number here.....: '))

print()

print('*** INFORMATION COLLECTED: TYPES OF MODULES ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** CONVERSION TO INTEGER ***')

print()

print('The value entered was {} and its Integer portion for CEIL......: {}' .format(num, ceil(num)))
print('The value entered was {} and its Integer portion for FLOOR.....: {}' .format(num, floor(num)))
print('The value entered was {} and its Integer portion for TRUNC.....: {}' .format(num, trunc(num)))
