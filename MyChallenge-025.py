# Criar um "PROGRAMA" que "LEIA" o "NOME COMPLETO" de uma Pessoa e
# verifique se ela possui ou não a Palavra: "SANTOS"

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 025: ***')

print()

nome = input('Whats your Name? ')

print()

nomecomp = str(input('Enter your full name here: ')).strip()

print()

print('*** INFORMATION COLLECTED: LOOKING FOR A STRING ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** LOOKING FOR NAME ***')

print()

print('Full Name......: {}'.format(nomecomp))

findname = 'Santos'

print()

print('Method 01:')

if findname.upper() in nomecomp.upper():
    print('The Name "{}" was found in the Phrase'.format(findname.upper()))
else:
    print('The Name "{}" was not found in the Phrase'.format(findname.upper()))

print()

print('Method 02:')

if nomecomp.count(findname) > 0:
    print('The Name "{}" was found in the Phrase'.format(findname))
else:
    print('The Name "{}" was not found in the Phrase'.format(findname))
