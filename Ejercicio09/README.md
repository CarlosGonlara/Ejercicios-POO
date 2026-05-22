# 📂 *__Ejercicio 09: Gestión de Archivos y Metadatos__*

Este repositorio presenta una solución práctica en **Python** para la creación de archivos de texto y la obtención de información técnica sobre su almacenamiento en disco, realizando cálculos de conversión a **KB** y **MB**.
para una manera mas rapida y precisa de verificar en mb o kbps el tamaño de los archivos de como quedaron cuando finalizamos el proyecto.

---

## 📝 *__Descripción del Proyecto__*

El programa demuestra el control de flujos de salida y el manejo del sistema de archivos mediante dos procesos clave:

1.  **Escritura Persistente:** Se genera un archivo llamado `Texto.txt` utilizando la codificación `utf-8` para garantizar la compatibilidad con caracteres especiales.
2.  **Análisis de Almacenamiento:** Mediante el módulo `os`, el script extrae el tamaño en *bytes* y aplica lógica matemática para mostrar el peso en unidades de almacenamiento estándar.



### 🛠️ *__Conceptos Aplicados__*

* 💾 **Manipulación de Archivos:** Uso de `open()`, `write()` y `close()` para persistencia de datos.
* 📐 **Cálculo de Unidades:** Conversión basada en potencias de 1024 ($1024^1$ para KB y $1024^2$ para MB).
* 📂 **Módulo OS:** Interacción directa con el sistema operativo para lectura de metadatos.



---

## 📂 *__Estructura del Proyecto__*

| 📄 Archivo | 🛠️ Propósito |
| :--- | :--- |
| `main.py` | *Código principal que crea el archivo y calcula su peso.* |
| `Texto.txt` | **Archivo generado** *dinámicamente por el script.* |
| `Ejercicio09/` | **Directorio contenedor** *del ejercicio.* |

