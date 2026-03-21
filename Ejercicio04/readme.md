# 💻 Ejercicio 04. Programación Orientada a Objetos (POO) en Python

Este repositorio contiene una serie de ejercicios desarrollados en **Python** para comprender y aplicar el concepto de **Herencia**. La práctica se divide en dos módulos: un sistema de gestión de menú para un restaurante y un sistema base para personajes de RPG.

---

## 🏗️ Conceptos Fundamentales
En ambos ejercicios se implementan los pilares de la POO:
* **Herencia:** Las subclases heredan atributos y métodos de una clase base.
* **Polimorfismo:** Los métodos con el mismo nombre se comportan de forma distinta según la clase.
* **Encapsulamiento Inicial:** Organización de datos mediante el constructor `__init__`.

---

## 🍽️ Módulo 1: Sistema de Restaurante

Este módulo gestiona los elementos de un menú, permitiendo diferenciar entre alimentos, bebidas y postres compartiendo una estructura de precios común.

### 📝 Estructura del Código
```python
class Platillo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def mostrar_info(self):
        print(f"{self.nombre} --- ${self.precio}")
        
    def tipo(self):
        print("...")

# Subclases: Comida, Bebida, Postre
