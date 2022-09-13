# Fazer um "PROGRAMA" que "LEIA" um "NÚMERO" de 0 até 9999 e mostra na "TELA" cada um dos Dígitos separados.

# Exemplo:

# Digite um Número: 1979
# Unidade.....: 9
# Dezena......: 7
# Centena.....: 9
# Milhar......: 1

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 023: ***')

print()

nome = input('Whats your Name? ')

print()

num = int(input('Enter the Number here: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print()

print('*** INFORMATION COLLECTED: SEPARATING DIGITS OF A NUMBER ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** NUMBERS ***')

print()

print('Analyzing the reported number: {}'.format(num))

print()

print('Unit.........: {}'.format(u))
print('Ten..........: {}'.format(d))
print('Hundred......: {}'.format(c))
print('Thousend.....: {}'.format(m))
