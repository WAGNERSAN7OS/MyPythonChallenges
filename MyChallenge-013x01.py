# Fazer um Algorítimo que "LEIA" o "PREÇO" de um "PRODUTO" e mostre seu novo "PREÇO",
# com 10% de "DESCONTO" se o Pagamento for a "VISTA" ou se o Pagamento for "PARCELADO"
# calcular o "AUMENTO" de 8% em cima do "VALOR DO PRODUTO".

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 013-01: ***')

print()

nome = input('Whats your Name? ')

print()

while True:

    print("""
        MENU
    ---------------
    1. A VISTA
    2. PARCELADO
    3. PIX
    0. EXIT
    """)

    opt = int(input('Option of Menu....: '))

    if opt == 0:
        break

    elif 1 <= opt <= 3:
        preco = float(input('Value of PRODUCT.......: R$'))
        print()

# Calculating with Operators (+, -, *, /):

# OPERATORS:

        while opt <= 3:
            if opt == 1:
                npreco = preco - (preco * descavt / 100)

            elif opt == 2:
                npreco = preco + (preco * descavt / 100)

            elif opt == 3:
                pix = preco - (preco * descavt / 100)

    else:
        print(' ***** Invalid Choice!!! *****')

print()

preco = float(input('Value of PRODUCT.......: R$'))
descavt = float(input('Value of DISCOUNT %....: '))
aumpcl = float(input('Value of DISCOUNT %....: '))

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
print('Discount......: {}%'.format(descavt))
print('-' * 25)
print('New Price.....: R${:.2f}'.format(aumpcl))

print()

print('The Product with a value of R${:.2f}, in the PROMOTION with {}% DISCOUNT, will COST R${:.2f}'.format(preco, descavt, aumpcl))
