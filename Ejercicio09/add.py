archivo = open("Ejercicio09/Texto.txt", "a", encoding="utf-8")
for i in range(1024**2):
    archivo.write("a")
archivo.close()