import random
numero_intentos = 1
numero_secreto = random.randint(1,100)
#print(numero_secreto)
numero_usuario = int(input("Ingrese un número: "))
print("Usted lleva ",numero_intentos," intento realizado de 7")
while(numero_secreto!=numero_usuario and numero_intentos != 7):
    if(numero_secreto > numero_usuario):
        print("El número secreto es mayor")    
    else:
        print("El número es Menor")
    numero_usuario = int(input("Ingrese un número: "))
    numero_intentos = numero_intentos + 1
    print("Usted lleva ",numero_intentos," intentos realizados de 7")
    

if(numero_secreto == numero_usuario):
        print("Felicidades, ¡Acertaste! al intento ",numero_intentos)
elif(numero_intentos == 7):
    print("Se acabaron las oportunidades el número secreto era ",numero_secreto)
   







