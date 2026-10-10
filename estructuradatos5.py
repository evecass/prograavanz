#Ejercicio 5. Detector de fraude y métricas de uso

#Construir dos contadores con Counter: expected_counter que representa el número de transacciones esperadas por categoría en un día normal (ej. {"restaurant": 10, "supermarket": 15, "technology": 2}) y daily_counter que representa las transacciones registradas el día de hoy (ej. {"restaurant": 12, "supermarket": 14, "technology": 9, "crypto": 4}).
#Utilizar la resta de contadores (daily_counter - expected_counter) para aislar los excesos no habituales registrados hoy.
#Utilizar .most_common(2) sobre el resultado para extraer e imprimir las 2 categorías con mayor desviación o exceso.
#Imprimir las categorías del día de hoy que nunca antes habían registrado operaciones utilizando la diferencia de conjuntos sobre las claves de los contadores.

# Importamos Counter desde collections. Counter permite contar la cantidad de veces que aparece cada elemento.
from collections import Counter

# Crear los dos contadores
# Este contador representa la cantidad de transacciones que normalmente se esperan en un día.
expected_counter = Counter({
    "restaurant": 10,
    "supermarket": 15,
    "technology": 2
})

# Este contador representa las transacciones registradas durante el día de hoy.
daily_counter = Counter({
    "restaurant": 12,
    "supermarket": 14,
    "technology": 9,
    "crypto": 4
})

# Imprimimos los contadores para observar sus valores.

print("Transacciones esperadas:")
print(expected_counter)

print("\nTransacciones registradas hoy:")
print(daily_counter)


# Calcular los excesos no habituales
# Restamos las transacciones esperadas de las registradas hoy.
# Counter elimina automáticamente los resultados que sean cero o negativos.

excess_counter = daily_counter - expected_counter

print("\nExcesos no habituales:")
print(excess_counter)


# Obtener las 2 categorías con mayor exceso
# most_common(2) obtiene las dos categorías que tienen los valores más altos dentro del contador.

top_excess = excess_counter.most_common(2)

print("\nLas 2 categorías con mayor desviación o exceso:")

for category, amount in top_excess:
    print(category, "->", amount, "transacciones de exceso")

# Encontrar categorías nuevas
# Obtenemos las categorías que existen en daily_counter pero que NO existen en expected_counter.
# Utilizamos la diferencia de conjuntos:

new_categories = daily_counter.keys() - expected_counter.keys()

print("\nCategorías nuevas que nunca antes habían registrado operaciones:")

for category in new_categories:
    print(category)