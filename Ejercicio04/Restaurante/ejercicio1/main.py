from Comida import Comida
from Bebida import Bebida
from Postre import Postre

tacos_de_pescado = Comida("Tacos de pastor", 30, "Principal")
limonada = Bebida("Limonada", 35, "Fria")
flan = Postre("Flan", 50, False)


print("--------------------------------")
lista = [tacos_de_pescado, limonada, flan]

for platillo in lista:
    print("Información de Platillo:")
    platillo.mostrar_info()
    platillo.tipo()
    print("-------------------------------")