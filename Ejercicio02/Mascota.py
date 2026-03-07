class Mascota:
    
    def __init__(self, nombre, tipo, edad, nivelFelicidad):
        
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.nivelFelicidad = nivelFelicidad
        
    def alimentar(self, puntos):
        if self.nivelFelicidad + puntos > 100:
            self.nivelFelicidad = 100
        else:
            self.nivelFelicidad += puntos

    def jugar(self, puntos):
        if self.nivelFelicidad + puntos > 100:
            self.nivelFelicidad = 100
        e151lse:
            self.nivelFelicidad += puntos
    
    def ignorar(self, puntos):
        if self.nivelFelicidad - puntos < 0:
            self.nivelFelicidad = 0
        else:
            self.nivelFelicidad -= puntos
    
    def mostrarEstado(self):
        return f"{self.nombre} es un {self.tipo}, tiene {self.edad} años \nSu nivel de felicidad es: {self.nivelFelicidad}"
    
    def esFeliz(self):
        return self.nivelFelicidad > 70

mascota1 = Mascota("Yuki", "Perro", "3", 80)
mascota2 = Mascota("Neko", "Gato", "6", 65)

mascota1.ignorar(25)
mascota1.alimentar(10)

mascota2.alimentar(10)
mascota2.jugar(20)
mascota2.alimentar(10)


print(mascota1.mostrarEstado())
print(f"¿Tu {mascota1.tipo} es feliz?: {mascota1.esFeliz()}")

print(mascota2.mostrarEstado())
print(f"¿Tu {mascota2.tipo} es feliz?: {mascota2.esFeliz()}")
