# Fazer um "PROGRAMA" que leia o comprimento do "CATETO OPOSTO" e do "CATETO ADJACENTE" de um "TRIÂNGULO RETÂNGULO".
# Calcular e Exibir o "COMPRIMENTO DA HIPOTENUSA".

"""
Relações Trigonométricas:

                30° 	45° 	60°
Seno........:   1/2 	√2/2 	√3/2
Cosseno.....:   √3/2 	√2/2 	1/2
Tangente....:   √3/3 	1       √3
"""

from math import hypot

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 017: ***')

print()

nome = input('Whats your Name? ')

print()

co = float(input('Length of the OPPOSITE CATHETER.....: '))
ca = float(input('Length of the ADJACENT CATHETER.....: '))

# Calculating with Operators (+, *):

# CALCULATIONS:

# h² = a² + b²

# hip = (co ** 2 + ca ** 2) ** (1/2)

hip = hypot(co, ca)

print()

print('*** INFORMATION COLLECTED: OPPOSITE CATHETER & ADJACENT CATHETER ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** LENGTH OF HYPOTENUSE ***')

print()

print('OPPOSITE CATHETER.....: {}'.format(co))
print('ADJACENT CATHETER.....: {}'.format(ca))
print('-' * 30)
print('HYPOTENUSE............: {:.2f}'.format(hip))

print()

print('For the CO we have {} and its CA we have {}, so the length of the HYPOTENUSE {:.2f}' .format(co, ca, hip))
