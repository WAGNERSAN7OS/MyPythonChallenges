# Criar um Script em Python que lei o "DIA", "MÊS", "ANO" de nascimento de uma pessoa
# e em seguida mostre uma "MENSAGEM" com a DATA "FORMATADA".

print(' +++++ @WAGNERSAN7OS +++++ ')

print('*** MY CHALLENGE 002: ***')

print()

nome = input('Whats your Name? ')

print('Please enter with your Date of Birth:')

dianasc = int(input('Day (dd)........: '))
mesnasc = int(input('Month (mm)......: '))
anonasc = int(input('Year (yyyy).....: '))

idadeatual = 2022 - anonasc

print()

print('*** INFORMATION COLLECTED: MY BIRTHDAY ***')

print()

print('Hello!..........:', nome)
print('Birthday........:', dianasc, '/', mesnasc, '/', anonasc)
print('Current Age.....:', idadeatual)
