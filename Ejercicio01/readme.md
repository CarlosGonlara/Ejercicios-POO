# Ejercicio 01: Clase Estudiante (POO)

Este repositorio contiene el ejercicio 01 de **Programación Orientada a Objetos** en Python, diseñado para modelar la gestión académica de un estudiante.

## Funcionalidades
* **Clase `Estudiante`**: Estructura principal con atributos de nombre, edad y carrera.
* **Gestión de Notas**: Permite añadir calificaciones dinámicamente.
* **Cálculo de Promedio**: Método para obtener la media aritmética de las notas.
* **Perfil de Usuario**: Genera una presentación del estudiante mediante f-strings.

## Ejemplo de Uso
```python
estudiante1 = Estudiante("Pako", 30, "Ing. en sistemas")
estudiante1.setCalificaciones(90)
print(estudiante1.mostrarInformacionUsuario())
