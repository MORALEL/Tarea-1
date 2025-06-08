class Alumno:
    def __init__(self, nombre, cedula, curso, nota):
        self.nombre = nombre
        self.cedula = cedula
        self.curso = curso
        self.nota = nota 

    def __str__(self):
        return f"{self.nombre} - {self.cedula} - {self.curso} - Nota: {self.nota}"

class GestorAlumnos:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, nombre, cedula, curso, nota):
        alumno = Alumno(nombre, cedula, curso, nota)
        self.alumnos.append(alumno)

    def consultar_alumnos(self):
        return self.alumnos

    def consultar_promedio(self):
        if not self.alumnos:
            return 0
        return sum(a.nota for a in self.alumnos) / len(self.alumnos)

    def clasificar_estudiantes(self):
        aprobados = [a for a in self.alumnos if a.nota >= 70]
        aplazados = [a for a in self.alumnos if 60 <= a.nota < 70]
        reprobados = [a for a in self.alumnos if a.nota < 60]
        promedio = self.consultar_promedio()
        superior = [a for a in self.alumnos if a.nota > promedio]
        return aprobados, aplazados, reprobados, superior
