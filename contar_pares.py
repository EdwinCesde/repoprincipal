mi_lista = []

# Preguntar al usuario cuántos números quiere ingresar
cantidad = int(input("¿Cuántos números quieres ingresar?: "))

# Usar un bucle para obtener los números
for i in range(cantidad):
    numero = float(input("Ingrese un número: "))
    mi_lista.append(numero)  # Agregar el número a la lista

# Mostrar la lista de números ingresados
print("Lista de números ingresados:", mi_lista)

#Funcion que cuenta lo numero pares
def contar_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador

#Se llama la funcion y se imprime el resultado
resultado = contar_pares(mi_lista)
print(resultado)