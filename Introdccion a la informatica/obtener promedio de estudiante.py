def llenarMatriz():
    global notas
    notas = []
  
    notas.append([0]*3)  
    
    print("Ingresa las notas para el estudiante: ")
    for j in range(3):
        notas[0][j] = int(input(f"Ingrese la nota {j + 1}: "))


def calculanota():
    notafinal = 0
    for j in range(3): 
        notafinal += notas[0][j]
    print(f"La nota final promedio del estudiante es: {notafinal / 3}")


notas = []
llenarMatriz()
calculanota()