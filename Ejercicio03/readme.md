# 🐾 Ejercicio 03.- Programacion Orientada a Objetos en Python: Herencia y Polimorfismo

Este repositorio contiene una implementación básica de **Programación Orientada a Objetos (POO)** utilizando Python, enfocándose en cómo las clases hijas pueden heredar y especializar el comportamiento de una clase padre.

---

## 🏗️ Estructura de Clases

La arquitectura del código se divide en una **Superclase** y dos **Subclases**:

### 1. Clase Padre: `Animal`
Es la base que define los atributos comunes para cualquier animal.
* **Atributos:** `nombre`, `edad`.
* **Métodos:** `describir()` (común) y `hablar()` (genérico).

### 2. Clases Hijas: `Perro` y `Gato`
Heredan todas las capacidades de `Animal` pero personalizan su comunicación.
* **Especialización:** Sobrescriben el método `hablar()` para emitir sonidos específicos.

---

## 💻 Código Fuente

```python
# --- Clase Base ---
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def describir(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")
    
    def hablar(self):
        print("...")

# --- Clases Derivadas ---
class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre}: ¡Guau!")
        
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre}: ¡Miau!")
