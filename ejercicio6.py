x = input('ingrese valor de primer numero: ')
y = input('ingrese valor de segundo numero: ')
z = input('ingrese valor de tercer numero: ')

def numer(x,y,z):
    if (x > y and x > z):
        print (x)
    if (y > x and y > z):
        print (y)
    if (z > x and z > y):
        print (z)

numer(x,y,z)