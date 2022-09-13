# Fazer um "PROGRAMA" que leia uma "FRASE" e mostre a formas de "STRING em "PYTHON".

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 022x01: ***')

print()

nome = input('Whats your Name? ')

print()

fullname = 'My first Python challenges in 2022'

print('*** INFORMATION COLLECTED: STRINGS in PYTHON ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** STRINGS ***')

print()

print('String Slicing: {}'.format(fullname))

print()

print('Show Index "9" inside the Phrase:', fullname[9])
print('Show Index "9" through "13" within the Phrase:', fullname[9:13])
print('Show Index "9" to "21" within the Phrase:', fullname[9:21])
print('Show Index "9" to "21" of "2 in 2" within the Phrase:', fullname[9:21:2])
print('Show the Index "5" on the LEFT within the Phrase:', fullname[:5])
print('Show the Index "15" on the RIGHT within the Phrase:', fullname[15:])
print('Show the Index "9" to the RIGHT of "3 in 3" within the Phrase:', fullname[9::3])

print('-' * 115)

print('String Analysis: {}'.format(fullname))

print()

print('Phrase Size:', len(fullname))
print('Count Letter(s) "n" in Phrase:', fullname.count('n'))
print('Count Letter(s) "n" from an Index in the Phrase:', fullname.count('n',0,30))
print('Show the Index of a Letter or Word "thon" in the Phrase:', fullname.find('thon'))
print('Find a Word "Android" in Phrase:', fullname.find('Android'))
print('Find a specific Word "Python" in Phrase:', 'Python' in fullname)

print('-' * 115)

print('String Transformation: {}'.format(fullname))

print()

print('Leave the entire Phrase in "UPPERCASE":', fullname.upper())
print('Leave the entire Phrase in "lowercase":', fullname.lower())
print('Leave the 1st letter of each "WORD" in "UPPERCASE":', fullname.title())
print('Leave the Letter of the 1st "WORD" in "UPPERCASE":', fullname.capitalize())
print('Change the Word "Python" to "ANDROID" in the Phrase:', fullname.replace('Python','ANDROID'))

print('-' * 115)

frase_02 = '   My first Python challenges in 2022   '

print('String Junction: {}'.format(frase_02))

print()

print('Delete "SPACES" at the BEGINNING and END of the Phrase:', frase_02.strip())
print('Delete "SPACES" at the beginning of the Phrase:', frase_02.lstrip())
print('Delete "SPACES" at the END of the Phrase:', frase_02.rstrip())
print('Make the Phrase CENTRALIZED:', frase_02.center(0))

print('-' * 115)

print('String Junction: {}'.format(fullname))

print()

print('Whatever "UPPERCASE" changes to "lowercase" in the Phrase:', fullname.swapcase())
print('Check if the entire Phrase is in UPPERCASE:', fullname.isupper())
print('Check if the entire Phrase is in LOWERCASE:', fullname.islower())
print('Check if the Phrase is ALPHANUMERIC:', fullname.isalnum())
print('Check if the Phrase is just ALPHA:', fullname.isalpha())
print('Check if the Phrase contains "SPACES":', ' '.isspace())

print('-' * 115)

print('String Division: {}'.format(fullname))

print()

print('Divide the Sentence by each WORD:', fullname.split())

print('-' * 115)

print('String Junction: {}'.format(fullname))

myjunc = fullname.split()

print()

print('Add the Phrase with SPECIAL CHARACTER "-":', '-'.join(myjunc))

print('-' * 115)

frase_03 = 'My first Python challenges in 2022. \n' \
          'The Python Language shows in a very practical and dynamic way how to solve various problems, \n' \
          'showing that Python is a high-level and easy-to-learn programming language.'

print('String Extra 01: {}'.format(frase_03))

print()

lista_01 = frase_03.split(' ')

palavra = ''
cont = 0

for valor in lista_01:
    qtd_x = lista_01.count(valor)

    if qtd_x > cont:
        cont = qtd_x
        palavra = valor

print('The Word that appears most in the Phrase was "{}", appearing in the total of "{}x"' .format(palavra, cont))

print('-' * 115)

frase_03 = 'My first Python challenges in 2022. \n' \
          'The Python Language shows in a very practical and dynamic way how to solve various problems, \n' \
          'showing that Python is a high-level and easy-to-learn programming language.'

print('String Extra 02: {}'.format(frase_03))

print()

lista_01 = frase_03.split(' ')

for valor in lista_01:

    print('The Word "{}", appearing in the total of "{}x"' .format(valor, lista_01.count(valor)))
