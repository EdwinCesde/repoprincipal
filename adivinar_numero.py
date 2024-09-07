import random

def adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 7
    
    print("¡Bienvenido al juego de adivinar el número!")
    print("He escogido un número entre 1 y 100.")
    print(f"Tienes {intentos_restantes} intentos para adivinarlo.\n")

    while intentos_restantes > 0:
        intento = int(input("Ingresa tu número: "))
        
        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} correctamente.")
            break
        elif intento < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        
        intentos_restantes -= 1
        
        if intentos_restantes > 0:
            print(f"Te quedan {intentos_restantes} intentos.\n")
        else:
            print(f"Lo siento, se te han acabado los intentos. El número era {numero_secreto}.")
    
# Ejecuta el juego
adivinar_numero()
