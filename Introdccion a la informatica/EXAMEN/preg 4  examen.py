# Se solicita al usuario que ingrese un número, que se almacena en la variable "numero"
numero = float(input("Por favor ingresar un numero: "))

# Validar si el numero es positivo, negativo o cero
if numero > 0:          #Se asegura que el numero sea mayor a 0, si es cierto imprime positivo
    print(f"El número {numero} es Positivo.")
#Si es cierto, imprime que el número es Positivo
#.
elif numero < 0:        #Se asegura que el numero sea menor a 0, si es cierto imprime negativo
    print(f"El número {numero} es Negativo.")
#Si es cierto, imprime que el número es negativo.

else:                   #si ninguna de las condiciones se cumplen, significa que el numero es 0
    print(f"El número {numero} es Cero.") 
#Se imprime un mensaje indicando que el número es cero.