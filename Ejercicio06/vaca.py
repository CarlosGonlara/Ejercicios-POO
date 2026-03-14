from mob import Mob

class Vaca(Mob):
    def __init__(self, nombre: str, vida: int):
        super().__init__(nombre, vida)

    def hacer_sonido(self) -> str:
        return "Muuu"

    def comportamiento(self) -> str:
        return "pasivo"

    def moverse(self) -> str:
        return "camina lento"