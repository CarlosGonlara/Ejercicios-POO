# 💻 Ejercicio 05. Programación Orientada a Objetos (POO) en Python
# 🧩 Abstracción en Python: Clases Abstractas (ABC)

Este ejercicio demuestra el uso del módulo `abc` (**Abstract Base Classes**) para definir interfaces obligatorias en una jerarquía de clases.

---

## 🧐 ¿Qué es una Clase Abstracta?

Una clase abstracta es una clase que **no se puede instanciar** directamente. Su único propósito es servir como un modelo o "plano" para otras clases. 

### 🔑 Componentes Clave:
1.  **`from abc import ABC, abstractmethod`**: Importación necesaria para habilitar la abstracción.
2.  **`class Animal(ABC)`**: Al heredar de `ABC`, definimos que esta clase es un concepto general, no un objeto real.
3.  **`@abstractmethod`**: Un decorador que obliga a las clases hijas (`Perro`, `Gato`) a escribir su propia versión del método `hablar()`. Si no lo hacen, Python lanzará un error.

---

## 💻 El Código: Implementación de Interfaz

```python
from abc import ABC, abstractmethod

# --- Clase Abstracta (El Contrato) ---
class Animal(ABC):
    @abstractmethod
    def hablar(self):
        """Este método DEBE ser implementado por cualquier subclase"""
        pass

# --- Clases Concretas (Implementación) ---
class Perro(Animal):
    def hablar(self):
        return "¡Guau!"

class Gato(Animal):
    def hablar(self):
        return "¡Miau!"
