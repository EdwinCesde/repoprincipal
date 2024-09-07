def promedio_notas(diccionario_notas):
    if not diccionario_notas:
        return 0
    suma_notas = 0
    
    for nota in diccionario_notas.values():
        suma_notas += nota
    
    promedio = suma_notas / len(diccionario_notas)
    
    return promedio


diccionario_notas = {
    'Juan': 4.5,
    'María': 4.0,
    'Pedro': 3.5
}

print(promedio_notas(diccionario_notas)) 
