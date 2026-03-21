# 💻 Ejercicio 06. Programación Orientada a Objetos (POO) en Python
# 👾 Sistema de Mobs: Abstracción y Polimorfismo en Videojuegos

Este módulo utiliza el concepto de **Clases Abstractas** para gestionar diferentes criaturas (mobs) de un mundo virtual, garantizando que todos compartan una estructura lógica mínima pero con comportamientos únicos.

---

## 🏛️ Arquitectura del Sistema: Clase `Mob`

La clase `Mob` actúa como un **contrato**. Define qué *debe* saber hacer una criatura, pero deja que cada especie decida *cómo* hacerlo.

### ✨ Elementos Técnicos:
* **Atributos Base:** Todos los mobs tienen un `nombre` y puntos de `vida` (HP).
* **Métodos Abstractos:** Se definen tres acciones obligatorias que cada subclase debe implementar:
    1.  `hacer_sonido()`
    2.  `comportamiento()`
    3.  `moverse()`
* **Método Concreto:** `presentarse()` es un método ya programado que utiliza los datos de los métodos abstractos para mostrar una ficha técnica del mob.

---

## 💻 Implementación del Código

```python
from abc import ABC, abstractmethod

class Mob(ABC):
    def __init__(self, nombre: str, vida: int):
        self.nombre = nombre
        self.vida = vida

    @abstractmethod
    def hacer_sonido(self) -> str: pass

    @abstractmethod
    def comportamiento(self) -> str: pass

    @abstractmethod
    def moverse(self) -> str: pass

    def presentarse(self):
        print(f"=== {self.nombre} ===")
        print(f"❤️  Vida       : {self.vida} HP")
        print(f"🔊  Sonido     : {self.hacer_sonido()}")
        print(f"⚔️  Tipo       : {self.comportamiento()}")
        print(f"🏃  Movimiento : {self.moverse()}")
        print()
