# Fazer um Algorítimo que "LEIA" o "PREÇO" de um "PRODUTO" e mostre seu novo "PREÇO",
# com 5% de "DESCONTO".

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 012: ***')

print()

nome = input('Whats your Name? ')

print()

preco = float(input('Value of PRODUCT.......: R$'))
desc = float(input('Value of DISCOUNT %....: '))

# Calculating with Operators (*, /):

# OPERATORS:

npreco = preco - (preco * desc / 100)

print()

print('*** INFORMATION COLLECTED: DISCOUNT PRICE ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** NEW PRICE ***')

print()

print('Price.........: R${:.2f}'.format(preco))
print('Discount......: {}%'.format(desc))
print('-' * 25)
print('New Price.....: R${:.2f}'.format(npreco))

print()

print('The Product with a value of R${:.2f}, in the PROMOTION with {}% DISCOUNT, will COST R${:.2f}'.format(preco, desc, npreco))
