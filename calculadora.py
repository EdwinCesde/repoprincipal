def calculadora():
    while True:
        print("\n--- Calculadora Básica ---")
        
        # Solicitar los números al usuario
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue  # Volver a iniciar el ciclo si hay un error de entrada

        # Seleccionar la operación
        print("\nSeleccione una operación:")
        print("1. Sumar (+)")
        print("2. Restar (-)")
        print("3. Multiplicar (*)")
        print("4. Dividir (/)")
        print("5. Salir")
        
        operación = input("Ingrese el número de la operación que desea realizar: ")

        # Realizar la operación seleccionada
        if operación == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif operación == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif operación == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif operación == '4':
            if num2 == 0:
                print("Error: No se puede dividir por cero.")
            else:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
        elif operación == '5':
            print("Saliendo de la calculadora...")
            break 
        else:
            print("Operación no válida. Intente de nuevo.")


calculadora()
