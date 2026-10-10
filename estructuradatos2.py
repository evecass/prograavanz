#EJERCICIO 2. Procesador de bitácoras y filtrado eficiente

#Dada la siguiente lista simulada de accesos a un servidor: logs = ["192.168.1.1 - GET", "10.0.0.5 - POST", "192.168.1.1 - GET", "172.16.0.2 - GET", "10.0.0.5 - POST", "192.168.1.1 - POST"] .
logs = [
    "192.168.1.1 - GET", 
    "10.0.0.5 - POST", 
    "192.168.1.1 - GET", 
    "172.16.0.2 - GET", 
    "10.0.0.5 - POST", 
    "192.168.1.1 - POST"] 

#Extraer únicamente la dirección IP de cada registro utilizando slicing o el método .split().
#Generar un conjunto (set) mediante Set Comprehension que contenga únicamente las IP únicas.

ips = {log.split(" - ")[0] for log in logs}

#Definir un segundo conjunto de IP bloqueadas: blocked_ips = {"10.0.0.5", "192.168.1.50"}.

blocked_ips = {"10.0.0.5", "192.168.1.50"}

#Utilizar la operación de diferencia de conjuntos (-) para obtener las IP permitidas que intentaron acceder al servidor e imprimir el resultado.

allowed_ips = ips - blocked_ips

print("IP permitidas:", allowed_ips)


