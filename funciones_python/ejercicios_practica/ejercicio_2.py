# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

from contextlib import nullcontext


def promedio(numeros):
    print("Funcion promedio")
        
    sumatoria_numeros=sum(numeros)
    cantidad_numeros=len(numeros)
    
    if cantidad_numeros==0:
        promedio=0
    else:
        promedio= sumatoria_numeros / cantidad_numeros
    
    return promedio

def resultado(resultado_promedio):
    if resultado_promedio>0:
        print('El promedio de notas ingresadas es : ', resultado_promedio)
    else:
        print('La lista no posee notas')
    
    # La función promedio recibe como parámetro una
    # lista de números. Con ella calcule el promedio como:
    # Aria y la cantidad con las herramientas
    # que desee, recomendamos usar las funciones disponibles
    # de Python para ello:    
    # sum --> obtener la sumatoria de números
    # len --> obtener la cantidad de números

    # La función debe retornar (return) el promedio calculado
    # La función debe contemplar si se le pasa una lista vacia
    # (es decir, de "0" elementos)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    numeros = [2,4,6,8,10,12]
 
    resultado_promedio = promedio(numeros)

    resultado=resultado(resultado_promedio)
 
    print("terminamos")
    
    
      # Alumno: Complete la función "promedio"

    # Llamar a la función en este lugar y capturar el valor del retorno
    # Luego imprimir en pantalla el valor resultante:
    # print(....)
    