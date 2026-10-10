#EJERICICIO 2
from matematica.operaciones import sumar
from matematica import geometria

resultado_suma = sumar(15, 25)
print("La suma de 15 + 25 es:", resultado_suma)

resultado_area = geometria.area_circulo(5)
print("El área del círculo con radio 5 es:", resultado_area)


#EJERCICIO 3

from procesador import titulo

cadena = "      hola    mundo     desde    python    "

resultado = titulo(cadena)

print("Texto original:", repr(cadena))
print("Texto procesado:", resultado)

#EJERCICIO 4

from reportes import *

print(crear_reporte_ventas(1500.50))

try:
    print(formatear_encabezado("PRUEBA"))

except NameError:
    print(
        "Error: formatear_encabezado no está disponible "
        "mediante la importación comodín."
    )
