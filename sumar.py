def suma_elementos():
    lista = []
    sum = 0
    max = int(input("¿cuántos números va a ingresar?: "))
    for i in range(max):
        num = int(input("Escriba un número: "))
        sum = sum + num
        lista.append(num)

    print ("Total: ",sum) 

suma_elementos()