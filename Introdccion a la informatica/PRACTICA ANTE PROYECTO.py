NOMBRE_LISTA = []

LISTA_DOSXDOS = []

"""
for i in range(4):
    elemento = input(f"Ingrese el elemento {i+1} : ")
    NOMBRE_LISTA.append(elemento)
    print("La lista es: ",NOMBRE_LISTA)
"""

#se ocupa un registro de estudiantes con notas y sus respectivos cursos

#Lista de estudiantes con 5 elementos (nombre de estudainte / nota)
#Lista de curso /materias (nombres de curso / nota)
#Las estructuras deben iniciar vacias y ser cargadas por teclado
#Las notas mas altas searan reconocidas con un premio de honor
#Los cursos seran reconocidos de mayor a menor segun su nota

#----------------Area De Analisis------------------#
#Definir o crear las estructuras de almacenamiento, lista de [5,2] vacias
#La lista 1 registra los estudiantes y sus notas 
#La lista 2 registrara los cursos o materias
#Obtener los datos de los estudiantes,notas,cursos y... 
#guardarlos en las estructuras por parte del usuario
#Proceso: Ordenamiento de las notas del estudiante
#Proceso: Ordenamiento de las notas de los cursos
#Proceso: Impresion de los resultados
#---------------------------------------------------#

LISTA_ESTUDIANTE = []
LISTA_CURSO = []


LISTA_DOSXDOS = [["Karla","Edwin"],[5,7]]
 
#print(LISTA_DOSXDOS)
 
 
def imprimirMatriz(LISTA_DOSXDOS):
    for i in range(len(LISTA_DOSXDOS[0])):
        print(LISTA_DOSXDOS[0][i], LISTA_DOSXDOS[1][i])
 
 
 
imprimirMatriz(LISTA_DOSXDOS)