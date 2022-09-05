# Escrever um Programa que "PERGUNTE" a quantidade de "KM" percorridos por um Carro Alugado
# e a quantidade de "DIAS" pelos quais o Veículo foi "ALUGADO".
# Calucular o "PREÇO A PAGAR", sabendo que o Carro custa "R$60,00" por Dia e R$0,15 por KM rodados.

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 015: ***')

print()

nome = input('Whats your Name? ')

print()

dias = int(input('Number of Days RENTED.....: '))
km = float(input('Number of KM TRAVELED.....: '))

# Calculating with Operators (+, *):

# CALCULATIONS:

pag = (dias * 60) + (km * 0.15)

print()

print('*** INFORMATION COLLECTED: CAR RENT ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** PAYMENT FOR RENT ***')

print()

print('DAYS........: {}'.format(dias))
print('KM..........: {}KM'.format(km))
print('-' * 25)
print('PAYABLE.....: R${:.2f}'.format(pag))

print()

print('For the number of {} Days the Vehicle was Rented and its current {}Km, the amount to be paid is R${:.2f}' .format(dias, km, pag))
