# Fazer um "PROGRAMA" que leia um "ÂNGULO QUALQUER" e mostre na tela o valor de "SENO", "COSSENO" e "TÂNGENTE"
# desse Ângulo.

"""
Relações Trigonométricas:

                30° 	45° 	60°
Seno........:   1/2 	√2/2 	√3/2
Cosseno.....:   √3/2 	√2/2 	1/2
Tangente....:   √3/3 	1       √3
"""

from math import radians, sin, cos, tan

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 018: ***')

print()

nome = input('Whats your Name? ')

print()

ang = float(input('Enter the value of the new ANGLE.....: '))

# Calculating with Operators (+, *):

# CALCULATIONS:

senno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print()

print('*** INFORMATION COLLECTED: SINE, COSINE and TANGENT ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** TRIGONOMETRIC CALCULATION ***')

print()

print('ANGLE.......: {}°'.format(ang))
print('-' * 20)
print('SINE........: {:.2f}'.format(senno))
print('COSINE......: {:.2f}'.format(coss))
print('TANGENT.....: {:.2f}'.format(tang))

print()

print('For the angle of {}° its SINE {:.2f}, its COSINE {:.2f} and its TANGENT {:.2f} ' .format(ang, senno, coss, tang))
