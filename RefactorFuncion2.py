#Funcion original
#Crear una lista de numeros, en este caso se genero una lista aleatoria de 3 digitos
#Imprimir dicha lista
#Tomar cada digito de la lista y multiplicarlo 3 veces, es decir, aplicarle el cubo
#Poner el resultado en una nueva lista
#Definir la condicion de fallo, que seria si la lista esta vacia. En este caso seria si el tamaño de la lista es menor a cero

# import random

# a= random.randrange(1, 10)
# b= random.randrange(1, 10)
# c= random.randrange(1, 10)
# mylist = [a, b, c]
# a = len(mylist)

# if a ==0:
#     print("Mensaje de error")

# print(mylist)
# d = a**3
# e = b**3
# f = c**3
# NewList = [d, e, f]
# print(NewList)

#Condicion de fallo
# bug_list = []
# b = len(bug_list)
# print(b)
# if b <=0:
#     print("Mensaje de error")

#*******Nueva funcion*******
#Mantenemos la funcion de crear cada valor de una lista con la funcion random de la funcion original
#Para esta funcion primero hacemos la funcion lambda con la condicion de multiplicar 3 veces el valor de "x", luego utilizamos la funcion map para poder hacerlo iterable
#y poder multiplicar cada elemento de la lista

import random

a= random.randrange(1, 10)
b= random.randrange(1, 10)
c= random.randrange(1, 10)
mylist = [a, b, c]
print(mylist)
new_list = list(map(lambda x : x**3, mylist))
print(new_list)