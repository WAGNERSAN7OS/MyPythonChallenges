# Escrever um Programa que "LEIA" quanto "DINHEIRO" uma pessoa tem "R$" na Carteira
# e "MOSTRAR" quanto em "DOLLAR" esta pessoa pode "COMPRAR".

"""
 *** Cotação DOLLAR US$:

 $ = 1,00

 *** Cotação REAL BRL:

 R$ = 5,50

"""

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 010: ***')

print()

nome = input('Whats your Name? ')

print()

print('Type Value in R$:')

print()

real = float(input('Value in REAL BRL.......: '))
dollar = float(input('Value in DOLLAR US$.....: '))

# Calculating with Operators (/):

# OPERATORS:

conv = real / dollar

print()

print('*** INFORMATION COLLECTED: REAL to DOLLAR ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** CURRENT CONVERSION ***')

print()

print('REAL.......: {} BRL'.format(real))
print('DOLLAR.....: {} US$'.format(dollar))
print('-' * 20)
print('Result.....: R${:.2f}'.format(conv))
