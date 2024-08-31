numeros = []
max = int(input("¿Cuantos números va a ingresar?"))

for i in range(max):
    num = int(input("ingrese un valor"))
    numeros.append(num)

def mas_grande(lista, maxi):
    grande = 0
    for i in range(maxi):
        if lista[i] > grande:
            grande = lista[i]
            print(grande)        
    

mas_grande(numeros, max)






