class profesor:
    def __init__(self, nombre, cedula, curso):
        self.nombre = nombre
        self.cedula = cedula
        self.curso= curso

    def __str__(self):
        return f"{self.nombre} - {self.cedula} - Curso: {self.curso} "
    
class GestorProfesores:
    def __init__(self):
        self.profesores = []

    def agregar_profesor(self, nombre, cedula, curso):
        nuevo_profesor = profesor(nombre, cedula, curso)
        self.profesores.append(nuevo_profesor)

    def consultar_profesores(self):
        return self.profesores
    