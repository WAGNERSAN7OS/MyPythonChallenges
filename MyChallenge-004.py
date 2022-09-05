# Fazer um Programa que leia algo pelo "TECLADO" e mostre na "TELA" o seu "TIPO PRIMITIVO"
# e todas as informações possíveis sobre ele.

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 004: ***')

print()

n = input('Type something her? ')

print()

print('*** INFORMATION COLLECTED: TYPES OF METHODS ***')

print()

print('What was typed is Alphabetic?.......: {}'.format(n.isalpha()))
print('What was typed is Alphanumeric?.....: {}'.format(n.isalnum()))
print('What was typed is Lower?............: {}'.format(n.islower()))
print('What was typed is Upper?............: {}'.format(n.isupper()))
print('What was typed is Numeric?..........: {}'.format(n.isnumeric()))
print('What was typed has Spaces?..........: {}'.format(n.isspace()))
print('What was typed is Capitalized?......: {}'.format(n.istitle()))