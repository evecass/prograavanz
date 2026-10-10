#EJERCICIO 3. Detector de mutabilidad y copia de objetos

#Crear un diccionario base que represente una plantilla de configuración de sistema: template = {"version": 1.0, "servers": ["alpha_server", "beta_server"], "active": True} .
#Crear shallow_config usando .copy() y deep_config usando copy.deepcopy().
#En shallow_config, modificar la clave "version" a 2.0 y agregar "gamma_server" a la lista "servers".
#En deep_config, agregar "delta_server" a la lista "servers".
#Imprimir la dirección de memoria de la lista de servidores (id(dict["servers"])) para los tres diccionarios (template, shallow_config y deep_config).
#Explicar mediante un comentario final en el código por qué la lista “servers” de la plantilla original fue modificada por shallow_config pero no por deep_config.

# Importamos el módulo copy para poder utilizar deepcopy()
import copy

# Crear un diccionario base que representa una plantilla de configuración del sistema.
template = {
    "version": 1.0,
    "servers": ["alpha_server", "beta_server"],
    "active": True
}

# Crear una copia superficial (shallow copy)
# .copy() crea un nuevo diccionario, pero los elementos internos
# como la lista "servers" siguen siendo compartidos.
shallow_config = template.copy()

# Crear una copia profunda (deep copy) deepcopy() crea una copia completamente independiente, incluyendo la lista que está dentro del diccionario.
deep_config = copy.deepcopy(template)


# Modificar shallow_config

# Cambiamos la versión únicamente en shallow_config.
shallow_config["version"] = 2.0

# Agregamos un nuevo servidor a la lista "servers".
shallow_config["servers"].append("gamma_server")

# Modificar deep_config

# Agregamos "delta_server" a la lista de servidores de la copia profunda.
deep_config["servers"].append("delta_server")


# Imprimir la dirección de memoria de la lista "servers" de cada uno de los tres diccionarios.

print("Dirección de memoria de la lista 'servers':")

print("template:", id(template["servers"]))
print("shallow_config:", id(shallow_config["servers"]))
print("deep_config:", id(deep_config["servers"]))


# También podemos imprimir los diccionarios para observar cómo quedaron después de las modificaciones.

print("\nContenido de los diccionarios:")

print("template:", template)
print("shallow_config:", shallow_config)
print("deep_config:", deep_config)

