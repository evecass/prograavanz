from .limpiador import quitar_espacios

def titulo(texto):
    texto_limpio = quitar_espacios(texto)
    return texto_limpio.title()
