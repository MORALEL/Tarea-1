
from alumnos import GestorAlumnos
from profesor import GestorProfesores
from cursos import GestorCursos

class SistemaEscolar:
    def __init__(self):
        self.cursos_validos = ["programacion", "calculo", "administracion", "ingles", "estructuras"]
        self.gestor_alumnos = GestorAlumnos()
        self.gestor_profesores = GestorProfesores()
        self.gestor_cursos = GestorCursos()

    def mostrar_menu(self):
        while True:
            print("\n Sistema Escolar")
            print("1. Agregar\\consultar Alumnos")
            print("2. Agregar\\consultar Profesores")
            print("3. Agregar\\consultar Cursos")
            print("4. Consultar reporte")
            print("5. Salir")

            opcion = input("Seleccione una opcion: ")
            if opcion == '1':
                self.menu_alumnos()
            elif opcion == '2':
                self.menu_profesores()
            elif opcion == '3':
                self.menu_cursos()
            elif opcion == '4':
                self.mostrar_reporte()
            elif opcion == '5':
                print("Salida Exitosa")
                break
            else:
                print("Opcion incorrecta. Intente de nuevo")

    def menu_alumnos(self):
        subopcion = input("a) Agregar Alumno \n b) Consultar Alumnos \n Seleccione una opcion: ").lower()
        if subopcion == 'a':
            nombre = input("Nombre alumno: ")
            nombre = nombre.title()
            if any(char.isdigit() for char in nombre):
                print("Error: El nombre no debe contener numeros")
                return

            cedula = input("Cedula alumno(11 digitos): ")
            if not (cedula.isdigit() and len(cedula) == 11):
                print("Error: La cedula debe tener 11 numeros")
                return
            curso = input("Curso alumno: ")
            if curso in self.cursos_validos:
                try:
                    nota = float(input("Nota alumno: "))
                    self.gestor_alumnos.agregar_alumno(nombre, cedula, curso, nota)
                except ValueError:
                    print("Error: La nota debe ser un número.")
            else:
                print("Error: El curso ingresado no está en la lista de cursos válidos.")
        elif subopcion == 'b':
            for a in self.gestor_alumnos.consultar_alumnos():
                print(a)
        else:
            print("Opcion Incorrecta")

    def menu_profesores(self):
        subopcion = input("a) Agregar profesor\n b) Consultar profesor\n Seleccione una opcion: ").lower()
        if subopcion == 'a':
            nombre = input("Nombre profesor: ")
            nombre = nombre.title()
            if any(char.isdigit() for char in nombre):
                print("Error: El nombre no debe tener numeros")
                return
            cedula = input("Cedula profesor: ")
            if not (cedula.isdigit() and len(cedula) == 11):
                print("Error: La cedula debe tener 11 numeros")
                return
            curso = input("Curso del profesor: ")
            self.gestor_profesores.agregar_profesor(nombre, cedula, curso)
        elif subopcion == 'b':
            for b in self.gestor_profesores.consultar_profesores():
                print(b)
        else:
            print("Opcion incorrecta")

    def menu_cursos(self):
        subopcion = input("a) Agregar curso\n b) Consultar cursos\n Seleccione una opcion: ").lower()
        if subopcion == 'a':
            print("Cursos válidos:", ", ".join(self.cursos_validos))
            curso = input("Nombre del curso: ")
            if curso in self.cursos_validos:
                codigo = input("Código del curso: ")
                self.gestor_cursos.agregar_curso(curso, codigo)
            else:
                print("Error: El curso ingresado no está en la lista de cursos válidos.")
        elif subopcion == 'b':
            for c in self.gestor_cursos.consultar_cursos():
                print(c)
        else:
            print("Opcion incorrecta")

    def mostrar_reporte(self):
        total_alumnos = self.gestor_alumnos.consultar_alumnos()
        print("Reporte General:")
        print("Total de alumnos registrados:", len(total_alumnos))
        print("Promedio de todas las notas de los alumnos:", self.gestor_alumnos.consultar_promedio())
        aprobados, aplazados, reprobados, superior = self.gestor_alumnos.clasificar_estudiantes()
        print("Estudiantes aprobados:", len(aprobados))
        print("Estudiantes aplazados:", len(aplazados))
        print("Estudiantes reprobados:", len(reprobados))
        print("Estudiantes con nota superior al promedio:", len(superior))

if __name__ == "__main__":
    sistema = SistemaEscolar()
    sistema.mostrar_menu()
