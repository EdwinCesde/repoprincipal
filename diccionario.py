alumnos = {}

while True:
    nombre = input("Ingresa el nombre del alumno (o 'salir' para terminar): ")

    if nombre.lower() == 'salir':
        break

    try:
        nota = float(input(f"Ingrese la nota de {nombre}: "))
    except ValueError:
        print("Por favor, ingresa una nota válida.")
        continue

    alumnos[nombre] = nota

print("\nLista de alumnos y sus notas:")
for nombre, nota in alumnos.items():
    print(f"{nombre}: {nota}")
