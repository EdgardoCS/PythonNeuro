import numpy as np

matrix = np.random.randint(low= 0, high = 2000, size=(6,10))
print(matrix)
maximo = np.max(matrix)
minimo = np.min(matrix)
print(maximo)
print(minimo)


a = np.array([(x-minimo)/(maximo-minimo)for x in range(60)])
print(a)
#Crear una matriz de 6x10 con números aleatorios. 
#Luego, buscar el máximo y el mínimo en la matriz
#Finalmente, normalizar cada elemento x de la matriz haciendo que sea igual a 
#(x - min)/(max-min). El último paso debe hacerse en una sola línea.