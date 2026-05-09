import os
ruta = "Ejercicio09/Texto.txt"
tamaño = os.path.getsize(ruta)
kb = tamaño / 1024
print(f"El tamaño del archivo es: {kb:.2f} KB")
mb = tamaño/ (1024 ** 2)
print(f"El tamaño del archivo es: {mb:.4f} MB")
