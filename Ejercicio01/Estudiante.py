# Esta es la clase
class Estudiante:
    #Aqui va es constructor
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    # Metodo para agregar calificaciones
    def setCalificaciones(self, calificacion):
        self.calificaciones.append(calificacion)
    
    # Metodo para calcular el promedio de calif.
    def mostrarPromedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    # Metodo para mostrar la informacion del usuario
    def mostrarInformacionUsuario(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}"


# Crear los objetos (instancias) de la clase
estudiante1 = Estudiante("Pako", 30, "Ing. en sistemas")
estudiante2 = Estudiante("Carmen", 25, "Ing. Industrial")
estudiante3 = Estudiante("Ramon", 20, "Ing. en Electronica")

print(estudiante1.mostrarInformacionUsuario())

estudiante1.setCalificaciones(75)
estudiante1.setCalificaciones(90)
print(f"La Calificacion es: {estudiante1.mostrarPromedio()}")