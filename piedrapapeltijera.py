print('Juego Del Piedra, Papel o Tijera')
#pequeño programa simple para jugar con una persona al piedra, papel o tijera.

jugador1 = input('Jugador 1 Ingresa (piedra , papel, tijera): ')
jugador2 = input('Jugador 2 Ingresa (piedra , papel, tijera): ')

if jugador1 == jugador2:
    print('Empate')
elif jugador1 == 'piedra' and jugador2 == 'papel':
    print(f'Jugador 2 Gana Saco {jugador2}')
elif jugador1 == 'papel' and jugador2 == 'piedra':
    print(f'Jugador 1 Gana Saco {jugador1}')
elif jugador1 == 'tijera' and jugador2 == 'papel':
    print(f'Jugador 1 Gana saco {jugador1}')
elif jugador1 == 'papel' and jugador2 == 'tijera':
    print(f'Jugador 2 Gana saco {jugador2}')
elif jugador1 == 'piedra' and jugador2 == 'tijera':
    print(f'Jugador 1 Gana saco {jugador1}')
elif jugador1 == 'tijera' and jugador2 == 'piedra':
    print(f'Jugador 2 Gana saco {jugador2}')


#Programa Super Basico con errores basicos, se puede ir mejorando y puliendo a medida mi experiencia avanza.