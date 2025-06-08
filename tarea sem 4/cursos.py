class curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Curso: {self.nombre}, Codigo: {self.codigo}"

class GestorCursos:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, nombre, codigo):
        nuevo_curso = curso(nombre, codigo)
        self.cursos.append(nuevo_curso)

    def consultar_cursos(self):
        return self.cursos
