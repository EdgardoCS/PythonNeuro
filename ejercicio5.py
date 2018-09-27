x = input('ingrese letra a evaluar: ')

def vocalmatic3000(x):
    
    if (x == 'a' or x =='e' or x == 'i' or x == 'o' or x== 'u'):
        print(True,';', x, 'es vocal')
    else: 
        print(False,';', x, 'es consonante')

vocalmatic3000(x)