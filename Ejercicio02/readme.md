# 💻 Ejercicio 2. Programación Orientada a Objetos (POO) en Python

Este repositorio contiene prácticas fundamentales de POO, enfocándose en la lógica de validación, el manejo de estados y el modelado de clases.

## 1. Cuenta Bancaria
Este ejercicio simula la gestión de una cuenta financiera básica, asegurando que las transacciones respeten las reglas de negocio (como no retirar más dinero del disponible).

```python
class CuentaBancaria:
    def __init__(self, titular, nCuenta, saldo):
        self.titular = titular
        self.nCuenta = nCuenta
        self.saldo = saldo

    def depositar(self, cant):
        self.saldo += cant
    
    def retirar(self, ret):
        if ret > self.saldo:
            print("❌ Fondos Insuficientes")
            return
        self.saldo -= ret
    
    def mostrarInformacion(self):
        return f"👤 {self.titular} | 💰 Saldo: {self.saldo}"
```
## 2. Mascota Virtual
Un sistema de control de estado emocional donde el nivel de felicidad está restringido a un rango específico mediante lógica matemática.

```python
class Mascota:
    def __init__(self, nombre, tipo, edad, nivelFelicidad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.nivelFelicidad = nivelFelicidad
        
    def alimentar(self, pts):
        self.nivelFelicidad = min(100, self.nivelFelicidad + pts)
        
    def jugar(self, pts):
        self.nivelFelicidad = min(100, self.nivelFelicidad + pts)
        
    def ignorar(self, pts):
        self.nivelFelicidad = max(0, self.nivelFelicidad - pts)
    
    def esFeliz(self):
        return self.nivelFelicidad > 70
```
🧠 Conceptos Aplicados
UML: Modelado de estructura de clases y sus interacciones.

Encapsulamiento: Implementación de reglas de negocio para la validación de rangos y saldos.

Lógica de Programación: Uso eficiente de funciones integradas como min() y max(), además de condicionales para el control de estados.
