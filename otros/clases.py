class Coche: #clase coche
    def __init__(self, Color, marca): #constructor
        self.color = Color
        self.marca = marca

    def describir(self): #imprimir
       print(f"este coche es de color {self.color} Marca = {self.marca}")

Toyota = Coche("Rojo", "Toyota")
Honda = Coche("Azul", "Honda") #instancia = copia de la clase

Toyota.describir()
Honda.describir()
