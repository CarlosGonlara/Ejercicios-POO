from mob import Mob

class Zombie(Mob):
    def __init__(self, nombre: str, vida: int):
        super().__init__(nombre, vida)

    def hacer_sonido(self) -> str:
        return "Grrrr"

    def comportamiento(self) -> str:
        return "agresivo"

    def moverse(self) -> str:
        return "camina lentamente"