#Escribir una función que tome un caracter (un texto de largo 1) 
#como argumento y devuelva True si es una vocal, False si no lo es.

# a = 1
# e = 5
# i = 9
# o = 16
# u = 22

def vocalmatic3000(x):
    
    if (x == 'a' or x =='e' or x == 'i' or x == 'o' or x== 'u'):
        print(True,';', x, 'es vocal')
    else: 
        print(False,';', x, 'es consonante')

vocalmatic3000('b')