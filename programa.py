class Human:

    # método constructor de la clase ÙwÚ
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    # método para mostrar la info de la persona ÙwÚ
    def show(self):
        print("nombre: " + self.nombre)
        print("apellidos: " + self.apellidos)
        print("edad: " + str(self.edad))

"""
def main():
    print("vamos a aprender POO...")
    persona_1 = Human("Pedro", "Pérez Pereira", 30)
    persona_1.show()

if __name__ == "__main__":
    main()

"""