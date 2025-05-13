list_numeros = [10, 5, 7, 2, 1]

#1. Imprimir la lista completa original
print("Lista original:")
print(list_numeros)

#2. Ordenar la lista e imprimirla completa.
list_numeros.sort()
print("\nLista ordenada:")
print(list_numeros)

# 3. Imprimir solo los (índices) impares de la lista.
print("\nÍndices impares de la lista ordenada:")
for indice in range(len(list_numeros)):
    if indice % 2 != 0:
        print(indice)