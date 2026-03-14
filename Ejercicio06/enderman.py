from mob import Mob

class Enderman(Mob):
    def __init__(self, nombre: str, vida: int):
        super().__init__(nombre, vida)

    def hacer_sonido(self) -> str:
        return "Sonido distorsionado"

    def comportamiento(self) -> str:
        return "Neutral"

    def moverse(self) -> str:
        return "se teletransporta"