lista = input("Ingresa una lista de números separados por coma: ")
lista = lista.split(",")

i = 0
while i < len(lista):
    #print(lista[i]) 
    lista_numeros = set(lista) 
    i += 1  

print(lista_numeros)