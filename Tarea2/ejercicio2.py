import numpy as np
cero = np.zeros((5,5))
ran = np.arange(5)
#print(cero)
#print(ran)

explicar = np.zeros((5,5)) + np.arange(5)
#print(explicar)
# zeros crea la matriz de 5x5 llena de 0, y se suma a arange la cual es [0 1 2 3 4]

uno = np.arange(7)[:,None]
dos = np.arange(5)
print(uno)
print("")
print(dos)
print("")
explicar2 = np.arange(7)[:,None] - np.arange(5)
print(explicar2)
#arange(7)[:,None] hace la matriz traspesta, y luego se resta cada elemento

