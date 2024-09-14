def buscar_palabra(diccionario, palabra):
    definicion = diccionario.get(palabra)
    if definicion:
        return f"Definición de '{palabra}': {definicion}"
    else:
        return f"La palabra '{palabra}' no se encontró en el diccionario."
    
diccionario = {
    "python": "Un lenguaje de programación de alto nivel.",
    "dictionario": "Una estructura de datos que almacena pares clave-valor.",
    "función": "Un bloque de código que se ejecuta cuando es llamado."
}


print(buscar_palabra(diccionario, "python"))
print(buscar_palabra(diccionario, "java"))
