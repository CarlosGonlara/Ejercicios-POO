from Aventurero import Aventurero

class Tanque(Aventurero):
    def __init__(self, nombre, nivel, armadura):
        super().__init__(nombre, nivel)
        self.armadura = armadura
        
    def usar_habilidad(self):
        print(f"{self.nombre} tiene  {self.armadura}! 🛡️")