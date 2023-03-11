#Funcion original

# N = input('Ingrese numero \n')
# num = int(N)
# if num <= 0:
#     print("Mensaje de error")
# i=0
# y=1
# for i in range(1,num+1):
#     y = y*i
# print(y)

#**********Nueva funcion**********
#Para este caso hacemos una lista de prueba, ejemplos
#Eliminamos de la lista los valores menores a 1, para no tener errores, y los guardamos en la lista filtrados
#la funcion lambda da como resultado un 1 si la x es igual que uno. De lo contrario se ejecuta la logica para obtener el factorial
#la utilizamos recursivamente para poder obtener el valor del factorial

ejemplos = [-1, 0, 1, 3, 4, 5]
filtrados = list(filter(lambda x: x >0, ejemplos))
for i in filtrados:
    factorial = lambda x: 1 if x == 1 else x * factorial(x-1)
    print(factorial(i))

