def promedio_notas():
    alumnos_notas = {}
    
    while True:
        nombre = input("Ingresa el nombre del alumno (o escribe 'fin' para terminar): ")
        
        if nombre.lower() == 'fin':
            break
        
        try:
            nota = float(input(f"Ingresa la nota de {nombre}: "))
            alumnos_notas[nombre] = nota
        except ValueError:
            print("Por favor, ingresa una nota válida.")
    
    if alumnos_notas:
        promedio = sum(alumnos_notas.values()) / len(alumnos_notas)
        print(alumnos_notas)
        print(f"\nEl promedio de las notas es: {promedio:.2f}")

    else:
        print("No se ingresaron notas.")

# Ejemplo de uso
promedio_notas()
