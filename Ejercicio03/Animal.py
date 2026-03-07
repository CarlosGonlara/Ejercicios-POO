#Clase padre
class Animal:
    #constructor
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def describir(self):
        print(f"Soy {self.nombre} y tengo {self.edad}")
    
    def hablar(self):
        print("...")
#------------------------------------------------------------------------
#Clase Derivada o Clase Hija
#------------------------------------------------------------------------        
    
class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre}: Guau!")
        
    
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre}: Miau!")