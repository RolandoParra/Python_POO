# Clase Persona

class Persona:
    
    # método constructor
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0

    def getNombre(self):
        return self.__Nombre
    
    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos
    
    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.__Nombre)
        print("Apellidos: " + self.__Apellidos)
        print("Edad: " + str(self.__Edad))

class Alumno(Persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
    
    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("Alumno")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tCurso: ", self.__Curso)
        print("\tMatrículas: ", self.__Asignaturas)

class Profesor(Persona):
    def __init__(self):
        self.__Departamento = ""
        self.__Asignaturas = ""
        self._cursos = ""
        self.__telefono= ""
        self.__email = ""
    
    def getDepartamento(self):
        return self.__Departamento
    def getAsignaturas(self):
        return self.__Asignaturas
    def setDepartamento(self, departamento):
        self.__Departamento = departamento
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas
    def getCursos(self):
        return self._cursos
    def setCursos(self, cursos):
        self._cursos = cursos
    def getTelefono(self):
        return self.__telefono
    def setTelefono(self, telefono):
        self.__telefono = telefono
    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email
    def mostrarProfesor(self):
        print("Profesor")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tDepartamento: ", self.__Departamento)
        print("\tAsignaturas: ", self.__Asignaturas)
        print("\tCursos: ", self._cursos)
        print("\tTeléfono: ", self.__telefono)
        print("\tEmail: ", self.__email)

# metodo principal
def main():
    alumno = Alumno()
    alumno.setNombre("Miku")
    alumno.setApellidos("Hatsune")
    alumno.setEdad(16)
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas(["Matemáticas", "Tecnología", "Inglés", "Física", "Química", "Historia", "Lengua", "Educación Física", "etc"])
    alumno.mostrarAlumno()

if __name__ == "__main__":
    main()