#desarrollar un algoritmo que lea dos valores y me de el mayor y el menor

#2 valores variables
#Tipos de variables numericos 
#Proceso de lectura de datos
#Proceso comparativo
#Proseso de resultados


#Inicio
#definir variables X, Y numericas 
#inicializar X = 0, Y = 0

#solicitar los 2 valores
#Leer X Y
#si X > Y entonces
#se devuelve X como mayor
#sino devuelve Y como Mayor

#Fin SI
#Fin

x = 0 
y = 0


#ingrese los valores de las variables
x = input("ingrese un valor: ")
y = input("ingrese un segundo valor: ")

if (x == y):
    print("los valores digitados son iguales, intente de nuevo")

if(x > y):
    print("el numero mayor es : ", x)
else:
    print("el numero mayor es : ", y)
