from utils import *
import random

def makeOneRun(distances):
    ''' Realiza el hash de una cadena de longitud aleatoria de bits 
    y una versión casi identica de la misma cadena. Luego calcula y
    devuelve la distancia de hamming entre los dos resultados.'''
    
    # Se elige el tamaño de la cadena. Solo se eligen longitudes multiplos
    # de 8 para poder hacer luego la conversión a bytes.
    l = random.randrange(8,1024,8)
    # Se selecciona la posicion de la cadena a cambiar.
    pos = random.randint(0,l-1)
    # Se genera la cadena aleatoria de bits de longitud l
    x1 = random.getrandbits(l)
    # Creamos la máscara apropiada y se la aplicamos al la primera
    # cadena para crear la cadena casi identica
    mask = 1 << pos
    x2 = x1 ^ mask

    # Generamos las cadenas de bits a partir de los enteros generados

    m1 = BitArray(uint=x1, length=l)
    m2 = BitArray(uint=x2, length=l)

    # Calculamos ambos hashes

    h1 = hashIt(m1.bytes)
    h2 = hashIt(m2.bytes)

    # Calculamos la distancia de hamming de los resultados y acumulamos 
    # el resultado.

    r1 = BitArray(h1)
    r2 = BitArray(h2)

    d = hammingDistance(r1,r2)
    distances[d-1] += 1

    # print(m1)
    # print(m2)
    # print(hammingDistance(m1,m2))
    # print(r1)
    # print(r2)
    # print(hammingDistance(r1,r2))

if __name__ == '__main__':
    testVectors()
    distances = [0] * 256
    for i in range(10000):
        makeOneRun(distances)

    print(distances)
    print(sum(distances))


