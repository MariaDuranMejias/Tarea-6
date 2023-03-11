#*****Funcion original*****
#Solicitarle al usuario 2 strings del mismo tamaño
#Verificar que las strings tengan el mismo tamaño
#En este caso se pone en una variable la longitud de las strings que ingreso el usuario
#Se comparan dichas variables par aver si son iguales, si son iguales se continua, si son diferentes se genera una condicion de error y se imprime un mensaje
#Si estas variables son iguales, se recorre cada strings y se guarda en una variable cada caracter de dicho string
#Poner en un nuevo arreglo el caracter 1 del primer string, luego el 1 del segundo string, y asi sucesivamente
#Se imprime el resultado eliminando los espacios entre iteraciones y resultados

# string1 = str(input('Ingrese 2 strings de mismo tamaño, string 1: \n'))
# string2 = str(input('string 2: \n'))

# x = int(len(string1))
# y = int(len(string2))
# if x != y:
#     print("Mensaje de error")
# elif x == y:
#     i=0
#     for i in range (0, x):
#         a = string1[i]
#         b = string2[i]
#         c = a+b
#         print(string1[i],string2[i],end=(''),sep=(''))


#****Funcion nueva*****
#le solicitamos al usuario que ingrese las 2 strings
#guardamos el valor de la longitud de ambas strings
# evaluamos si son de mismo tamaño
#sino lo son, se devolvera un mensaje de error
#si lo son se procede a recorrer ambas strings
#se aplica la funcion lambda con un parametro j y la expresion sera la suma de cada caracter de las strings intercaladas
string1 = str(input('Ingrese 2 strings de mismo tamaño, string 1: \n'))
string2 = str(input('string 2: \n'))

x = int(len(string1))
y = int(len(string2))
if x != y:
    print("Mensaje de error")
elif x == y:
    i=0
    for i in range (0, x):
        funcion = lambda j : string1[j] + string2[j]
        print(funcion(i),end=(''),sep=(''))
