

#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez"]

#lista_frutas = ["Mango", "Piña", "Banano"]

#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] para el remove


#lista_marcas.len

#tamano = (len(lista_marcas))

#print(len(lista_marcas))  #muestra la cantidad de elementos que hay en la lista

#print(lista_marcas)

#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#for lista_marcas in lista_marcas:    #llamar una lista asia abajo
#    print(lista_marcas)


#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#print(lista_marcas[1]) #llamar una sola marca


#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#print(f"El elemento que esta en la tercera pocision es {lista_marcas[2]} que es la mejor marca") #saca el elemento en la tercera pocision

#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#print(lista_marcas[4][7]) #saca una letra de un arreglo de la lista 


#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#print(lista_marcas[-1]) #sacar los elementos de la lista de atras para adelante


#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#lista_marcas[3] = "Volkswagen" #asignar nuevos elementos a la lista
#print(lista_marcas)

#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Mercedez", "Toyota"] 
#lista_marcas.append("Volvo") #agregar un nuevo elemento a la lista
#print(lista_marcas)
#print(len(lista_marcas))


#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#lista_marcas.insert(1, "BYD")   #dar la pósicion en la que se quiere poner un nuevo elemento
#print(lista_marcas)


#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#lista_marcas.clear()   #se limpia la lista de todos los datos
#print(lista_marcas)
#print(len(lista_marcas))

#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#lista_marcas.pop(1)  #se elimina un elemento determinado
#print(lista_marcas)

#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#lista_marcas.remove("Toyota") #busca las mismas palabras para elimar y dejar solo uno
#print(lista_marcas)


#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#lista_marcas = lista_marcas
#print("Duplicacion de listas")     # DUPLICA LAS LISTAS
#print(lista_marcas)
#print(lista_marcas)


#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#print(lista_marcas.count("Toyota"))   # Dice la cantidad de elementos duplicados
 
#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#print("El elemento encontrado esta en :")
#print(lista_marcas.index("Toyota"))   

#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#print("OTRA DUPLICACION DE LISTAS")
#L2 = lista_marcas.copy()
#print(L2)

#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#print("La lista ordenada Al reves es : ")     #pone el orden de la lista al reves
#lista_marcas.reverse()
#print(lista_marcas)


#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#print("La lista ordenada es : ")     #pone en orden alfabetico ascendente la lista
#lista_marcas.sort()
#print(lista_marcas)


#lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez", "Toyota"] 
#print("La lista ordenada es : ")     #pone en orden alfabetico descendente la lista
#lista_marcas.sort(reverse=True)
#print(lista_marcas)


lista_marcas = ["Toyota", "Hyundai", "Nisan", "Volvo", "Mercedez"]
lista_frutas = ["Mango", "Piña", "Banano"]
lista_marcas.extend(lista_frutas)      #Une una lista con otra lista
print("La lista extendida es: ")
print(lista_marcas)