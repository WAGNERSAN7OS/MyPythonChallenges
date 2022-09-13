# Criar um PROGRAMA que "LEIA" o "NOME COMPLETO" de uma Pessoa e mostre:

# O seu Nome com todas as Letras "MAIÚSCULAS";
# O seu Nome com todas as Letras "minúculas";
# Contar quantas "LETRAS" o Nome possui, sem contar os "ESPAÇOS";
# Contar quantas "LETRAS" tem o primeiro "NOME".

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 022: ***')

print()

nome = input('Whats your Name? ')

print()

fullname = str(input('Enter your full name here: '))

print()

print('*** INFORMATION COLLECTED: STRINGS in PYTHON ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** MY STRINGS ***')

print()

print('String Analysis: {}'.format(fullname))

print()

print('Analyzing the STRING...')

print()

print('Leave the entire Name in "UPPERCASE".....: {}'.format(fullname.upper()))
print('Leave the entire Name in "lowercase".....: {}'.format(fullname.lower()))
print('Name length not counting "SPACES"........: {}'.format(len(fullname.strip()) - (fullname.count(' '))))
print('Your first Name has a total of...........: {} Letters'.format(fullname.find(' ')))

print('-' * 75)

print('Second Option for 1st Name:')

print()

divname = fullname.split()

print('Your first Name is.......................: {}'.format(divname[0]))
print('Your first Name has a total of...........: {} Letters'.format(len(divname[0])))
