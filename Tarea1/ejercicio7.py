x = input('ingrese valor de primer numero: ')
y = input('ingrese valor de segundo numero: ')
z = input('ingrese valor de tercer numero: ')

x = int(x)
y = int(y)
z = int(z)

def histogram(x,y,z):
    lst = [x,y,z]
    for a in range (0,len(lst)):
        # print (lst[a])
        b = lst[a]
        ast = []
        for a in range (0,b):
            ast.append('*')
        print(ast, b)


histogram(x,y,z)