def alumno_con_mejor_nota(alumnos_notas):
    mejor_alumno = None
    mejor_nota = -1  # Se usa -1 porque las notas no pueden ser negativas

    for alumno, nota in alumnos_notas.items():
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = alumno
    
    return mejor_alumno

alumnos_notas = {
    "Juan": 85,
    "Ana": 92,
    "Pedro": 78,
    "Lucía": 88
}

mejor_alumno = alumno_con_mejor_nota(alumnos_notas)
print(f"El alumno con la mejor nota es: {mejor_alumno}")
