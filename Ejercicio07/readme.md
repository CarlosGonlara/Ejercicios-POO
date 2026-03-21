# 💻 Ejercicio 07. Programación Orientada a Objetos (POO) en Python
# Manejo de Excepciones en Python

Este documento contiene un ejemplo práctico sobre cómo gestionar errores comunes utilizando los bloques `try`, `except`, `else` y `finally`.

## Parte 1: División con manejo de errores

El siguiente script solicita dos números al usuario y realiza una división, protegiendo el programa de entradas inválidas o divisiones por cero.

```python
print("="*50)
print("Parte 1: División con manejo de errores")
print("="*50)

try:
    # Intentamos convertir la entrada a entero y realizar la división
    a = int(input("Ingrese el numerador: "))
    b = int(input("Ingrese el denominador: "))
    resultado = a / b

except ValueError:
    # Se ejecuta si el usuario ingresa texto en lugar de números
    print("Error: Debe ingresar un número entero, no una letra.")

except ZeroDivisionError:
    # Se ejecuta si el denominador es 0
    print("Error: No se puede dividir por cero.")
    
else:
    # Se ejecuta solo si NO hubo ninguna excepción
    print(f"El resultado de {a} dividido por {b} es: {resultado}")

finally:
    # Se ejecuta siempre, ocurra o no un error
    print("Operación de división finalizada.")