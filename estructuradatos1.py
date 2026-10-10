#EJERCICIO 1. Modelado de datos y validador de tipos

#Crear una estructura de datos que represente una base de datos de usuarios donde cada usuario tenga: ID (entero), Name (string) y Coords (latitud, longitud).
#Utilizar un diccionario como contenedor principal, donde la clave sea una tupla formada por (ID, Name) y el valor sea la tupla de coordenadas.

usuarios = {
    (1, "Evelyn"): (19.24, -103.72),
    (2, "Carlos"): (19.43, -99.13),
    (3, "Ana"): (20.67, -103.35)
}

#Intentar agregar un usuario cuya clave contenga una lista en lugar de una tupla (ejemplo: ([101, "Carlos"], (19.43, -99.13))) dentro de un bloque try-except para capturar el error TypeError explícitamente e imprimir un mensaje explicativo.

try:
    usuarios[([101, "Carlos"])] = (19.43, -99.13)
except TypeError:
    print("Error: no se puede utilizar una lista como clave de un diccionario porque las listas son mutables.")

#Iterar sobre la base de datos e imprimir el nombre y coordenadas de cada usuario registrado.

for clave, coordenadas in usuarios.items():
    id_usuario, nombre = clave
    print("Nombre:", nombre)
    print("Coordenadas:", coordenadas)
    



