import numpy as np

ar1 = np.ones((8,8))
print(ar1)
print("")

ar8 = np.ones((5,15))*8
print(ar8)
print("")

num = np.random.normal(loc=15,scale=5,size=(6,6))
print(num)
print("")

D = np.random.randint(low= 0, high = 20, size=(7,9))
print(D)
print("")

print("max(D)", np.max(D))
print("min(D)", np.min(D))
print("max, axis=0 (columnas)", np.max(D,axis = 0))
print("min, axis=1 (filas)", np.min(D,axis = 1))
print("np.argmax (filas)", np.argmax(D,axis=1)) #posicion del valor máximo"
print("D>10", D>10)
print("1*", 1*(D>10))
print("")

tryar = np.random.randint(low=0,high=22, size=(7,9))
print(np.max(tryar))
print(np.max(D))
print("")
print(np.maximum(D,tryar))



