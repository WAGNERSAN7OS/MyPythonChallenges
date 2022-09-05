# Fazer um Programa que leia um "NÚMERO INTEIRO" qualquer e mostre na "TELA" a sua Tabuada "CONVERTIDA".

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 009: ***')

print()

nome = input('Whats your Name? ')

print()

while True:

    print("""
        MENU
    ---------------
    1. ADDITION
    2. SUBTRACTION
    3. MULTIPLICATION
    4. DIVISION
    5. POTENCY
    6. WHOLE DIVISION
    7. REST
    0. EXIT
    """)

    opt = int(input('Option of Menu....: '))

    if opt == 0:
        break

    elif 1 <= opt <= 7:
        n = int(input('Table Value.......: '))
        cont = 1
        print()

# Calculating with Operators (+, -, *, /, **, //, %):

# OPERATORS:

        while cont <= 10:
            if opt == 1:
                print('{} + {:2} = {}'.format(n, cont, (n + cont)))

            elif opt == 2:
                print('{} - {:2} = {}'.format(n, cont, (n - cont)))

            elif opt == 3:
                print('{} x {:2} = {}'.format(n, cont, (n * cont)))

            elif opt == 4:
                print('{} / {:2} = {:.2f}'.format(n, cont, (n / cont)))

            elif opt == 5:
                print('{} ** {:2} = {}'.format(n, cont, (n ** cont)))

            elif opt == 6:
                print('{} // {:2} = {}'.format(n, cont, (n // cont)))

            elif opt == 7:
                print('{} % {:2} = {}'.format(n, cont, (n % cont)))
            cont = cont + 1

    else:
        print(' ***** Invalid Choice!!! *****')

print()

print('*** INFORMATION COLLECTED: TABLE ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** MULTIPLICATION TABLE ***')

print()

if opt == 1:
    print('Table ADDITION (+) {}:'.format(opt))

    if opt == 2:
        print('Table SUBTRACTION (-) {}:'.format(opt))

    if opt == 3:
        print('Table MULTIPLICATION (x) {}:'.format(opt))

    if opt == 4:
        print('Table DIVISION (/) {}:'.format(opt))
else:
    print('THANKS!!!')
