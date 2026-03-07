# 🏦 Ejercicio 02: Sistema de Cuenta Bancaria (POO)

Este repositorio contiene una implementación práctica de la **Programación Orientada a Objetos (POO)** en Python, enfocada en la simulación de transacciones bancarias básicas.

## 📝 Descripción del Proyecto
El objetivo de este ejercicio es modelar el comportamiento de una cuenta de banco mediante una clase. El sistema permite gestionar el saldo de diferentes usuarios, validando que las operaciones de retiro sean seguras y no excedan el capital disponible.

## 🛠️ Funcionalidades Principales
* **Instanciación de Cuentas**: Creación de múltiples perfiles con titular, número de cuenta y saldo inicial.
* **Método `depositar`**: Incrementa el saldo de la cuenta de forma sencilla.
* **Método `retirar`**: Implementa una **validación lógica** para evitar retiros si los fondos son insuficientes.
* **Consultas de Estado**: Métodos para obtener el saldo actual y un resumen general formateado.

---

## 💻 Código Fuente

```python
class CuentaBancaria:
    
    def __init__(self, titular, nCuenta, saldo):
        """Constructor para inicializar los datos de la cuenta."""
        self.titular = titular
        self.nCuenta = nCuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        """Suma una cantidad al saldo actual."""
        self.saldo += cantidad
    
    def retirar(self, retiro):
        """Resta una cantidad si hay fondos suficientes."""
        if retiro > self.saldo:
            print(f"❌ Fondos Insuficientes para {self.titular}")
            return 0
        self.saldo -= retiro
    
    def consultarSaldo(self):
        """Devuelve un mensaje con el saldo disponible."""
        return f"El saldo actual es de ${self.saldo} pesos"
    
    def mostrarInformacion(self):
        """Muestra un resumen del estado de la cuenta."""
        return f"👤 Titular: {self.titular} | 💰 Saldo: ${self.saldo}"

# --- Instanciación de Objetos ---
cuenta1 = CuentaBancaria("Carlos Gonzalez", "0001", 1000.00)
cuenta2 = CuentaBancaria("Samanta Alcantara", "0002", 500.00)
cuenta3 = CuentaBancaria("Jolliete Alcantara", "0003", 200.00)

# --- Pruebas de Funcionamiento ---
cuenta1.retirar(500.00)
print(cuenta1.mostrarInformacion())

cuenta3.retirar(500.00)  # Esto dispar