def multiplicar_elementos(lista):
    nueva_lista = [] 
    for elemento in lista:
        nueva_lista.append(elemento * 2)  # Multiplica cada elemento por 2 y lo agrega a la nueva lista
    return nueva_lista

def solicitar_lista_usuario():
    lista = []
    while True:
        numero = input("Ingrese un número (o 's' para terminar): ")
        if numero == 's':
            break
        else:
            try:
                lista.append(float(numero))  # Convertir a número y agregar a la lista
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return lista

# Solicitar la lista y mostrar la lista multiplicada
lista_usuario = solicitar_lista_usuario()
nueva_lista = multiplicar_elementos(lista_usuario)
print("Lista original:", lista_usuario)
print("Lista multiplicada por 2:", nueva_lista)
