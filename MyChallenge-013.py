# Fazer um Algorítimo que "LEIA" o "SALÁRIO" de um "FUNCIOÁRIO" e mostre seu "NOVO SALÁRIO",
# com 15% de "AUMENTO".

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 013: ***')

print()

nome = input('Whats your Name? ')

print()

salario = float(input('Value of WAGE...........: R$'))
acres = float(input('Value of INCREASE %.....: '))

# Calculating with Operators (+, *, /):

# CALCULATIONS:

nsalario = salario + (salario * (acres / 100))

print()

print('*** INFORMATION COLLECTED: SALARY INCREASE ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** NEW WAGE ***')

print()

print('Wage.........: R${:.2f}'.format(salario))
print('Increase.....: {}%'.format(acres))
print('-' * 25)
print('New Wage.....: R${:.2f}'.format(nsalario))

print()

print('The Wage actual is R${:.2f}, and with INCREASE of {}%, the Employee receive R${:.2f}'.format(salario, acres, nsalario))
