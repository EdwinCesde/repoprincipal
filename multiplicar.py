def multiplicar_elementos():
    lista_multi= []
    lista = []
    max = int(input("¿cuántos números va a ingresar?: "))
    for i in range(max):
        num = int(input("Escriba un número: "))
        lista.append(num)
        lista_multi.append(num*2)

    print (lista) 
    print (lista_multi)

multiplicar_elementos()
