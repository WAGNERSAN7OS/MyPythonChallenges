# Desenvolver um Programa que leia duas "NOTAS" de um Aluno(a),
# faça o "CALCULO" entre essas Notas e mostre na tela a sua "MÉDIA".

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 007: ***')

print()

nome = input('Whats your Name? ')

print()

print('Please enter with Integer Value:')

print()

note1 = float(input('Note 01.....: '))
note2 = float(input('Note 02.....: '))

# Calculating with Operators (+, /):

media = (note1 + note2)/2

print()

print('*** INFORMATION COLLECTED: MEDIA ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('Note 01.....: {}'.format(note1))
print('Note 02.....: {}'.format(note2))
print('-'*20)
print('Media.......: {}'.format(media))

print()

if media >= 7:
    print('Student.....: {}'.format(nome), '\nSituation.....: APROVADO!!!')
else:
    print('Student.....: {}'.format(nome), '\nSituation.....: REPROVADO!!!')
