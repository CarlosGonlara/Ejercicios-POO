from mob import Mob

class Creeper(Mob):
    def __init__(self, nombre: str, vida: int):
        super().__init__(nombre, vida)

    def hacer_sonido(self) -> str:
        return "Sssss"

    def comportamiento(self) -> str:
        return "agresivo"

    def moverse(self) -> str:
        return "corre hacia el jugador"