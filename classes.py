class Human:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    # método para mostrar la info de la persona ÙwÚ
    def show(self):
        print("nombre: " + self.nombre)
        print("apellidos: " + self.apellidos)
        print("edad: " + str(self.edad))


class coordenada:
    # metodo constructor UwU
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # método gatuncito
    def show(self):
        print("(", self.x, self.y, ")")


class cuadrado:
    def __init__(self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
    
    def show(self):
        print("el cuadrado está compuesto por los siguientes vértices: ")
        self.v1.show()
        self.v2.show()
        self.v3.show()
        self.v4.show()