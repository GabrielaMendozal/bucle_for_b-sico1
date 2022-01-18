#Básico: imprime todos los números enteros del 0 al 150.

for num in range (0,151):
    print (num)


#Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.    

def numeros_multiplos (limite_inferior, limite_superior):
    resultado = []
    for n in range (limite_inferior,  limite_superior  +   1):
        if n % 5 ==0:
            resultado.append(n)

    return resultado

numeros = numeros_multiplos (5, 1000)
print (numeros)

#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. 
#Si es divisible por 5, imprime "Coding” en su lugar. 
#Si es divisible por 10, imprime "Coding Dojo".

for i in range (0 , 101):
    if i %10 ==0:
        print("Coding Dojo")
    elif i %5 ==0:
        print("Coding")
    else:
        print(i)

#Whoa. Es una gran idea

suma=0
for i in range (1, 500001,2):
    suma+=i
print(suma)

# 
for i in range (2018,0,-4):
    print (i)

# 

menor = 2
mayor = 9
m = 3 

for i in range (menor,mayor+1):
    if i %m == 0:
        print (i)