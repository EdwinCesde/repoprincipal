diccionario = {}

while True:
    palabra = input("Introduce una palabra (o escribe 'salir' para terminar): ").lower()
    
    if palabra == 'salir':
        break
    
    definicion = input(f"Introduce la definición de '{palabra}': ")
    
    diccionario[palabra] = definicion
    print(f"\n'{palabra}' ha sido agregada al diccionario.\n")


print("\nDiccionario completo:")
for palabra, definicion in diccionario.items():
    print(f"{palabra}: {definicion}")