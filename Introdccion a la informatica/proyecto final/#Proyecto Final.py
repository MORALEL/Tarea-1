#Proyecto Final
#Crear las listas de los paises y los puntos
grupoA = ["Japon", "España", "Costa Rica", "Zambia"]

grupoB = ["China", "Dinamarca", "Inglaterra", "Haití"]

puntosA = [0,0,0,0]
puntosB = [0,0,0,0]

#Ingresar puntos a cada equipo
for i in range(4):
    puntosA[i] = int(input(f"ingrese los puntos para {grupoA[i]}: "))
    while puntosA[i] < 0 or puntosA[i] > 9:
        print("Error: Los puntos deben estar entre 0 y 9")
        puntosA[i] = int(input(f"ingrese los puntos para {grupoA[i]}: "))
        

    puntosB[i] = int(input(f"ingrese los puntos para {grupoB[i]}: "))
    while puntosB[i] < 0 or puntosB[i] > 9:
        print("Error: Los puntos deben estar entre 0 y 9")
        puntosB[i] = int(input(f"ingrese los puntos para {grupoB[i]}: "))

#Combinar equipos con sus puntos
grupoA_puntos = list(zip(grupoA, puntosA))
grupoB_puntos = list(zip(grupoB, puntosB))

#Funcion para ordenenar por puntos
def obtener_puntos(equipo):
    return equipo[1]

#Ordenar equipos por puntos 
grupoA_puntos = sorted(grupoA_puntos, key=obtener_puntos, reverse=True)
grupoB_puntos = sorted(grupoB_puntos, key=obtener_puntos, reverse=True)

#Mostrar pocisiones Finales
print("\nPocisiones finales del Grupo A\n")
for equipo, puntos in grupoA_puntos:
    print(f"{equipo} : {puntos} puntos")


print("\nPocisiones finales del Grupo B\n")
for equipo, puntos in grupoB_puntos:
    print(f"{equipo} : {puntos} puntos")

#Mostrar cruces de octavos de final
print("\nCruces de Octavos de Final:")
print(f"{grupoA_puntos[0][0]} vs {grupoB_puntos[1][0]}")
print(f"{grupoB_puntos[0][0]} vs {grupoA_puntos[1][0]}")
