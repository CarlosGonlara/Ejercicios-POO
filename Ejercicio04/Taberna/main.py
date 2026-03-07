from Guerrero import Guerrero
from Mago import Mago
from Arquero import Arquero
from Tanque import Tanque

guerrero_1 = Guerrero("Leonidas", 90, "Espada")
mago_1 = Mago("Megumin", 85, "Explosion")
arquero_1 = Arquero("Diana", 92, 20 )
tanque_1 = Tanque("Garen", 88, "Armadura de acero")
print("--------------------------------")
lista = [guerrero_1, mago_1, arquero_1, tanque_1]

for Aventurero in lista:
    print("Información de Personaje:")
    Aventurero.presentarse()
    Aventurero.usar_habilidad()
    print("-------------------------------")