def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0
    i = 0

    while i < len(frase):
        if frase[i] in vocales:
            contador += 1
        i += 1
    
    return contador

frase_usuario = input("Ingresa una frase: ")

cantidad_vocales = contar_vocales(frase_usuario)
print(f"La frase contiene {cantidad_vocales} vocales.")
