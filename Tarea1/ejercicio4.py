#jan ken pon

P1 = input('Jugador1: Jan, Ken, Pon? ')
# if (P1 != 'piedra' or P1 != 'papel' or P1 != 'tijera'):
#     print('Solo puedes ingresar: piedra, papel o tijera') 

P2 = input('Jugador2: Jan, Ken, Pon? ')
# if (P2 != 'piedra' or P2 != 'papel' or P2 != 'tijera'):
#     print('Solo puedes ingresar: piedra, papel o tijera') 
draw = 0
if (P1 == P2):
    print ('empate')
    draw = 1

if (draw != 1):
    if (P1 == 'piedra' and P2 == 'tijera' or P1 == 'papel' and P2 == 'piedra' or P1 == 'tijera' and P2 == 'papel'):
        print('Gana Jugador1')
    else:
        print ('Gana Jugador2')