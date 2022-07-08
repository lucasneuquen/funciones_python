# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.2

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios con funciones y módulos
import random
from re import I

'''
Enunciado:
Alumno: Crear la función "contar"

Utilice la función "lista_aleatoria" creada antes 
para generar una lista de 5 números en
un rango de 1 a 6 inclusive

lista_numeros = lista_aleatoria(inicio, fin, cantidad)

Generar una una nueva funcion que se llame "contar",
que cuente la cantidad de veces que un número (pasado
por parámetro a la función) se repite en la lista (también pasada por parámetro)

Para saber cuantas veces se repiten el elemento pasado
en la lista pueden usar el método nativo de list "count"
'''

# --------------------------------
# Aquí copiar la función "lista_aleatoria"
# ya elaborada en el ejercicio anterior

def lista_aleatoria(inicio,fin,cantidad):
    
    lista_aleatoria=[]
    while cantidad>0:
        numero = random.randint(inicio, fin)
        lista_aleatoria.append(numero)
        cantidad=cantidad-1

    return lista_aleatoria
# --------------------------------

# --------------------------------
# Aquí dentro definir la función contar
def contar(lista_numeros,valor):
    tres=0
    for i in lista_numeros:
        if i==3:
            tres=tres+1
  
    return tres
# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Utilizar la función "lista_aleatoria"
    # para que genere una lista de 5 números que esten comprendidos
    # entre los números 1 al 6 inclusive
    inicio = 1
    fin = 6
    cantidad = 5
    lista_numeros = lista_aleatoria(inicio,fin,cantidad)

    # Imprimir en pantalla "lista_numeros" que tendrá
    # los valores retornado por la función "lista_aleatoria":

    print('La lista aleatoria es: ',lista_numeros)

    # Luego quiero averiguar cuantas veces se repite el numero 3
    # en la lista aleatoria creada
    
    cantidad_tres = contar(lista_numeros,3)
    
    print('En la lista hay ',cantidad_tres, 'tres')

    print("terminamos")
