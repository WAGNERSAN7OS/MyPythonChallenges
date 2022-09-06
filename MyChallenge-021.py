# Fazer um Programa em PYTHON que consiga "ABRIR" e "REPRODUZIR" um Arquivo do tipo "MP3"

# import pygame
# pygame.init()

from pygame import mixer

mixer.init()

print(' +++++ @WAGNERSAN7OS +++++ ')

print()

print('*** MY CHALLENGE 021: ***')

print()

nome = input('Whats your Name? ')

print()

print('*** INFORMATION COLLECTED: MUSIC PLAYER ***')

print()

print('*** Welcome!!! ***')

print()

print('+++++ {}'.format(nome), '+++++')

print()

print('*** MUSIC ***')

mixer.music.load('CDZ_Abel_Theme.mp3')
mixer.music.play()
mixer.music.set_volume(0.7)

while True:

    print('Press "P" to PAUSE Music.')
    print('Press "R" to SUMMARIZE Music.')
    print('Press "E" to EXIT the Player.')

    comando = input(' ')

    if comando == 'P':
        mixer.music.pause()
    elif comando == 'R':
        mixer.music.unpause()
    elif comando == 'E':
        mixer.music.stop()
    break
