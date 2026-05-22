# 🏆 *__Sistema de Gestión de Torneo (POO)__*

Este repositorio contiene una implementación **robusta** y *profesional* en **Python** para la gestión de usuarios en un entorno de torneo. El proyecto se centra en demostrar los pilares fundamentales de la **Programación Orientada a Objetos (POO)**, tales como la *herencia*, el *encapsulamiento* y la *especialización de clases*.

<div align="center">
  </div>

---

## 📝 *__Descripción del Proyecto__*

El sistema está diseñado para modelar el comportamiento de diferentes tipos de participantes. Utiliza una **arquitectura jerárquica** donde una clase base define el comportamiento común, mientras que las clases derivadas añaden funcionalidades específicas según el rol del usuario.

### 🧬 *__Jerarquía de Clases__*

La estructura se divide en tres niveles principales:

* 🥇 **`Jugador` (_Clase Base_):**
  * **Función:** Actúa como el molde general para cualquier usuario.
  * **Atributos:** Almacena datos esenciales como el *nombre*, *número de control* y *nivel de habilidad*.

* ⚔️ **`Competidor` (_Clase Hija_):**
  * **Especialización:** Usuarios activos que participan en el torneo.
  * **Atributos extra:** Gestión de pertenencia a un *equipo*.
  * **Lógica:** Implementa métodos para la gestión dinámica de puntos (**`ganar_puntos`** / **`perder_puntos`**).
  * **Polimorfismo:** Sobrescribe el método `mostrar_perfil()` utilizando `super()` para extender la funcionalidad base.

* 👁️ **`Observador` (_Clase Hija_):**
  * **Especialización:** Usuarios dedicados al análisis y visualización de partidas.
  * **Lógica:** Incluye un contador interno mediante el método **`ver_partida()`**.

---

## 📂 *__Estructura de Archivos__*

| 📄 Archivo | 🛠️ Descripción |
| :--- | :--- |
| `main.py` | *Punto de entrada que orquesta la ejecución y pruebas del sistema.* |
| `Jugador.py` | **Clase base** *y definición de la lógica compartida.* |
| `Competidor.py` | **Clase hija** *con la implementación de competencia y equipos.* |
| `Observador.py` | **Clase hija** *con la implementación de la lógica de espectadores.* |
