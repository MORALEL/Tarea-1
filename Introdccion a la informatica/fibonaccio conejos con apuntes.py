# Definir la lista Fibonacci con los primeros dos términos
fibonacci = [1, 1]

# Calcular la Secuencia hasta el mes 12
for i in range(2, 13):  # desde el mes 2 hasta el mes 12
    nuevoTerm = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(nuevoTerm)

# Imprimir resultados para cada mes
for mes in range(13):  # para los meses del 0 al 12
    if mes < 2:
        paresInicio = 0  # al inicio del mes 0 y 1 no hay pares nacidos
        paresNacidos = 1
    else:
        paresInicio = fibonacci[mes - 1]
        paresNacidos = fibonacci[mes - 2]
    
    paresFinal = paresInicio + paresNacidos
    
    print(f"Mes {mes}: ParesInicio = {paresInicio}, ParesNacidos = {paresNacidos}, ParesFinal = {paresFinal}")