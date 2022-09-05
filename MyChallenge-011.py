# Fazer um Programa que "LEIA" a "LARGURA" e a "ALTURA" de uma parede em "METROS",
# calcule a sua "ÁREA" e a quantidade de "TINTA" necessária para Pintá-la,
# sabendo que cada "LITRO DE TINTA", pinta uma Área de "2m²".

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 011: ***')

print()

nome = input('Whats your Name? ')

print()

alt = float(input('Value of Height.....: '))
larg = float(input('Value of Width......: '))

# Calculating with Operators (*, /):

# OPERATORS:

area = alt * larg

ltinta = area / 2

print()

print('*** INFORMATION COLLECTED: AREA ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** CURRENT CONVERSION ***')

print()


print('HEIGHT.....: {}m'.format(alt))
print('WIDTH......: {}m'.format(larg))
print('-' * 20)
print('AREA.......: {}m²'.format(area))

print()

print('Your Wall has {}mx{}m and your Area {}m².'.format(alt, larg, area))
print('To Paint this Wall of {}m², you will need {}l of Paint.'.format(area, ltinta))
