#Ejercicio 4. Modelado de transacciones e ingestión en tiempo real

#Crear un tipo de dato inmutable llamado Transaction usando namedtuple con los campos: id (entero), user (string), amount (flotante) y category (string).
#Instanciar un buffer circular con deque definiendo un tamaño máximo de 5 elementos (maxlen=5).
#Insertar secuencialmente 7 objetos Transaction simulando la llegada de eventos en tiempo real.
#Verificar e imprimir que el tamaño del deque no supere los 5 elementos y mostrar cómo las transacciones más antiguas se descartaron automáticamente.
#Ejecutar una rotación del buffer (rotate(2)) e imprimir el estado resultante.

# Importamos namedtuple para crear un tipo de dato inmutable e importamos deque para crear el buffer circular.
from collections import namedtuple, deque

# 1. Crear el tipo de dato Transaction

# namedtuple permite crear una estructura similar a una clase,
# pero sus datos son inmutables, es decir, no se pueden modificar después de crear el objeto.

Transaction = namedtuple(
    "Transaction",
    ["id", "user", "amount", "category"]
)


# Crear un buffer circular con máximo 5 elementos

# deque permite almacenar elementos de manera eficiente. maxlen=5 significa que el buffer solamente puede contener como máximo 5 elementos.
# Cuando se agrega un sexto elemento, el más antiguo se elimina automáticamente.

buffer = deque(maxlen=5)


# Insertar 7 objetos Transaction

# Creamos e insertamos las transacciones una por una, simulando eventos que llegan en tiempo real.

transactions = [
    Transaction(1, "Ana", 150.50, "Comida"),
    Transaction(2, "Luis", 300.00, "Transporte"),
    Transaction(3, "Maria", 89.99, "Entretenimiento"),
    Transaction(4, "Carlos", 450.75, "Comida"),
    Transaction(5, "Sofia", 120.00, "Ropa"),
    Transaction(6, "Pedro", 75.50, "Transporte"),
    Transaction(7, "Laura", 600.00, "Tecnologia")
]


# Insertamos cada transacción en el buffer.
for transaction in transactions:
    buffer.append(transaction)

    print("Se agregó:", transaction)
    print("Tamaño actual del buffer:", len(buffer))
    print("Contenido:", list(buffer))
    print("-" * 60)


# Verificar que el deque no supere los 5 elementos

print("\nBUFFER FINAL")
print("=" * 60)

print("Tamaño máximo permitido:", buffer.maxlen)
print("Tamaño actual:", len(buffer))
print("Contenido final:")

for transaction in buffer:
    print(transaction)


# Verificamos que el buffer no tenga más de 5 elementos.
if len(buffer) <= 5:
    print("\nEl buffer NO supera los 5 elementos.")
else:
    print("\nError: el buffer supera los 5 elementos.")


# Las primeras dos transacciones (ID 1 y 2) fueron descartadas automáticamente cuando llegaron las transacciones 6 y 7.

# Esto ocurre porque el deque tiene maxlen=5.
# Cuando se intenta agregar un nuevo elemento y el buffer ya está lleno, se elimina automáticamente el elemento más antiguo.

# Rotar el buffer utilizando rotate(2)

print("\nBUFFER ANTES DE LA ROTACIÓN")
print("=" * 60)

print(list(buffer))


# rotate(2) mueve los últimos 2 elementos hacia el inicio
# del deque.
buffer.rotate(2)


print("\nBUFFER DESPUÉS DE rotate(2)")
print("=" * 60)

print(list(buffer))