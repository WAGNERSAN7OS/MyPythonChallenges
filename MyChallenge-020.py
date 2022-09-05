# O mesmo Professor do desafio anterior, quer sortear a ordem de apresentação de Trabalhos dos Alunos.
# Fazer um "PROGRAMA" que leia os seus Nomes e que mostre a ordem sorteada.

# import shuffle

from random import shuffle

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 020: ***')

print()

nome = input('Whats your Name? ')

print()

name1 = input('Enter with a Name.....: ')
name2 = input('Enter with a Name.....: ')
name3 = input('Enter with a Name.....: ')
name4 = input('Enter with a Name.....: ')
name5 = input('Enter with a Name.....: ')

list = [name1, name2, name3, name4, name5]

shuffle(list)

print()

print('*** INFORMATION COLLECTED: ORDER OF PRESENTATION ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** PRESENTATION ***')

print()

print('The order of presentation will be.....: {}'.format(list))
