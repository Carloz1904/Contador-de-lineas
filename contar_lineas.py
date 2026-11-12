import sys

def contar_lineas(archivo):
    with open(archivo,"r", encoding="utf-8") as f:
        contenido = sum (1 for _ in f)
    print(f'El archivo tiene {contenido} lineas')


if len(sys.argv) !=2:
    print("Uso: python3 {sys.argv[0]} archivo.txt")
    sys.exit(1)

archivo_texto = sys.argv[1]

try:
    contar_lineas(archivo_texto)
except FileNotFoundError:
    print(f'NO encontre el archivo "{archivo_texto}". Revisa el nombre y la carpeta.')