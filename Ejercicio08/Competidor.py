from Jugador import Jugador

class Competidor(Jugador):
    def __init__(self, nombre: str, num_control: str, nivel: str, equipo: str):
        super().__init__(nombre, num_control, nivel)
        self.equipo = equipo

    def mostrar_perfil(self):
        super().mostrar_perfil()
        print(f"Equipo: {self.equipo}")