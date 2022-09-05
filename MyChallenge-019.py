# Um Professor quer sortear um dos seus Quatro Alunos para apagar o Quadro.
# Fazer um "PROGRAMA" que ajude Ele, lendo os seus Nomes e que mostre o NOME do Aluno ESCOLHIDO.

# import random

from random import choice

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 019: ***')

print()

nome = input('Whats your Name? ')

print()

name1 = input('Enter with a Name.....: ')
name2 = input('Enter with a Name.....: ')
name3 = input('Enter with a Name.....: ')
name4 = input('Enter with a Name.....: ')
name5 = input('Enter with a Name.....: ')

lista = [name1, name2, name3, name4, name5]

# nomesc = random.choice(lista)

nomesc = choice(lista)

print()

print('*** INFORMATION COLLECTED: RANDOM CHOICE ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** NAME CHOSEN ***')

print()

print('The name chosen was.....: {}'.format(nomesc))
