# Criar um "PROGRAMA" que "LEIA" o "NOME DE UMA CIDADE" e
# verifique se ela começa ou não com o Nome: "SANTOS"

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 024: ***')

print()

nome = input('Whats your Name? ')

print()

cidade = str(input('Enter City Name: ')).strip()

print()

print('*** INFORMATION COLLECTED: CHECKING FIRST NAME ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** FIRST WORD ***')

print()

print('Name of the City.....: {}'.format(cidade))
print('First Name...........:', cidade[:6].upper() == cidade.upper().split()[0])
