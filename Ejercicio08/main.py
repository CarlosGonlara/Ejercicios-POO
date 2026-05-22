from Competidor import Competidor
from Observador import Observador

def ejecutar_torneo():
    print("--- Competidor ---")
    c1 = Competidor("CarlosGLZ", "25760802", "Leyenda", "Equipo 23")
    c1.mostrar_perfil()
    print()
    c1.ganar_puntos(100)
    c1.perder_puntos(10)

    print("\n--- Observador ---")
    o1 = Observador("Linda Ann", "20023110", "principiante")
    o1.ver_partida()
    o1.ver_partida()
    o1.mostrar_perfil()

if __name__ == "__main__":
    ejecutar_torneo()