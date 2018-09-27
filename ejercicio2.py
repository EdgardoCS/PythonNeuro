n = input('ingrese valor de n: ')

n = int(n)

i = 1
lst = []
for a in range(1,n+1):
    
    i=i*a
    lst.append(i)

print(lst)
lst.reverse()
print(lst)
    
