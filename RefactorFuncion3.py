#*******Funcion original********
# def potencia():  #Se crea una funcion que permite al usuario ingresar n numeros y cumpla su funcion de potencia
#     n1 = int(input("Ingrese el primer numero:  "))  #Se le solicita al usuario el primer digito
#     n2 = int(input("Ingrese el segundo numero:  "))  # Se le solicita al usuario el segundo digito

#     resultado = n1 ** n2  # Se crea la variable resultado que sera igual a la multiplicaion de ambos digitos ingresados por el usuario
#     return resultado  # # Con la funcion return la variable del resultado hara el print con el resultado de la potencia


#*********Nueva Funcion*******
#Le solicitamos los 2 numeros que se van a multi[licar al usuario
#definimos los parametros de la funcion lambda
#la expresion va a ser la multiplicacion de estos numeros
#imprimimos el resultado
n1 = int(input("Ingrese el primer numero:  "))  
n2 = int(input("Ingrese el segundo numero:  "))
resultado = lambda n1, n2: n1*n2
print(resultado(n1,n2))