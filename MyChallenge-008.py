# Escrever um Programa que leia um "VALOR" em "METROS" e em seguida o exiba "CONVERTIDO"
# em "CENTIMETROS" e "MILIMETROS".

"""
 *** Múltiplos de Metros:

 Quilômetro (Km) :  1M / 1000 = 1Km
 Hectômetro (Hm) :  1M / 100  = 1Hm
 Decâmetro (Dam) :  1M / 10   = 1Dam

 *** Submultiplos de Metros:

 Milímetro (mm)  :  1M * 1000 = 1mm
 Centímetro (cm) :  1M * 100  = 1cm
 Decímetro (dm)  :  1M * 10   = 1dm

"""

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 008: ***')

print()

nome = input('Whats your Name? ')

print()

print('Please enter with Integer or Float Value:')

print()

met = float(input('Value in Meters.....: '))

# Calculating with Operators (*, /):

# MULTIPLES OF METERS:

km = met / 1000
hec = met / 100
dam = met / 10

# SUBMULTIPLES OF METERS:

mil = met * 1000
cent = met * 100
dec = met * 10

print()

print('*** INFORMATION COLLECTED: CENTIMETERS and MILIMETER ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** SUBMULTIPLES OF METERS ***')

print()

print('Value in M (Meters)...........: {:.0f}M'.format(met))
print('Value in mm (Millimeters).....: {:.0f}mm'.format(mil))
print('Value in cm (Centimeters).....: {:.0f}cm'.format(cent))
print('Value in dm (Decimeters)......: {:.0f}dm'.format(dec))

print()

print('*** MULTIPLES OF METERS ***')

print()

print('Value in Km (Kilometers)......: {}Km'.format(km))
print('Value in Hm (Hectometers).....: {}Hm'.format(hec))
print('Value in Dam (Dekameters).....: {}Dam'.format(dam))
