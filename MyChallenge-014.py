# Escrever um Programa que "CONVERTA" uma "TEMPERATURA" digitado em °C - CELCIUS
# e a "CONVERTA" para °F - FAHRENHEIT.

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 014: ***')

print()

nome = input('Whats your Name? ')

opt = -1

while opt != 0:

    print("""
        MENU
    ---------------
    1. CELSIUS to FAHRENHEIT
    2. FAHRENHEIT to CELSIUS
    0. EXIT
    """)

    opt = int(input('Option of Menu....: '))

    if opt == 0:
        break

    print()
    
    print('Type Value in °C and °F: ')

    print()

# Calculating with Operators (+, -, *, /):

# OPERATORS:

    if opt == 1:
        C = float(input('Graus Celsius: '))
        F = (C * 9 / 5) + 32
        print('FAHRENHEIT.....: {}°F'.format(F))

    elif opt == 2:
        F = float(input('Graus Farenheit: '))
        C = (F - 32) * 5 / 9
        print('CELSIUS.......: {}°C'.format(C))

else:
    print('Opção Inválida!!!')

print()

print('*** INFORMATION COLLECTED: CELSIUS to FAHRENHEIT ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** CURRENT CONVERSION ***')

print()

print('THANKS!!!')
