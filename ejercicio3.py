n = 30

divisores = []

for a in range(2,n+1):
    
    c = float(n%a)

    if c == 0.0:
        divisores.append(a)

if len(divisores)==1:
    print(n,'es primo')
else:
    print(n,'no es primo')
    print('divisores de',n,':', divisores)