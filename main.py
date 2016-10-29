from utils import hashIt, testVectors, hammingDistance
from bitstring import BitArray
import random
import statistics
import datetime

def makeOneRun():
    ''' Realiza el hash de una cadena aleatoria de bits 256
    y una copia de la cadena con un bit complementado. Luego calcula y
    devuelve la distancia de hamming entre los dos resultados.'''
    
    # Se selecciona la posicion de la cadena a cambiar.
    pos = random.randint(0,255)
    # Se genera la cadena aleatoria de 256 bits de longitud
    x1 = random.getrandbits(256)

    # Creamos la máscara apropiada y se la aplicamos a la primera
    # cadena para crear la cadena casi identica
    mask = 1 << pos
    x2 = x1 ^ mask

    # Generamos las cadenas de bits a partir de los enteros generados
    m1 = BitArray(uint=x1, length=256)
    m2 = BitArray(uint=x2, length=256)

    # Calculamos ambos hashes
    h1 = hashIt(m1.bytes)
    h2 = hashIt(m2.bytes)

    # Calculamos la distancia de hamming de los resultados y acumulamos 
    # el resultado.

    r1 = BitArray(h1)
    r2 = BitArray(h2)

    return hammingDistance(r1,r2)


if __name__ == '__main__':

    testVectors()
    
    distances1 = []
    distances2 = []    # Listas para acumular resultados de las corridas
    distances3 = []
    n = 100              # Numero de hashes a probar en cada corrida

    ##################
    #
    # Primera corrida
    #
    ##################

    for i in range(n):
        distances1.append(makeOneRun())

    # Calculamos el error de la media con respecto a 
    # la media ideal que es 256/2 = 128
    m1 = statistics.mean(distances1)
    error1 = abs(128 - m1)/128

    # Abortamos si el error es mayor a 5% (0.05)
    if error1 > 0.05:
        raise RuntimeError("La primera corrida dio un error mayor a 5%")

    ##################
    #
    # Segunda corrida
    #
    ##################

    # Repetimos el proceso de la primera corrida
    for i in range(n):
        distances2.append(makeOneRun())
    m2 = statistics.mean(distances2)
    error2 = abs(128 - m2)/128
    if error2 > 0.05:
        raise RuntimeError("La segunda corrida dio un error mayor a 5%")

    ##################
    #
    # Tercera corrida
    #
    ##################

    for i in range(n):
        distances3.append(makeOneRun())
    m3 = statistics.mean(distances3)
    error3 = abs(128 - m3)/128
    if error3 > 0.05:
        raise RuntimeError("La tercera corrida dio un error mayor a 5%")

    ###############################
    #
    # Calculo final de resultados
    #
    ###############################

    f = open('Resultado-' + str(datetime.date.today()) + '.txt','w')
    f.write("Experimento del dia " + str(datetime.date.today()) + ".\n")

    # Acumulamos el resultado de las tres corridas
    result = distances1 + distances2 + distances3

    # Calculamos los estadisticos correspondientes
    # y los escribimos al archivo de salida
    media = statistics.mean(result)
    f.write("Media: " + str(media) + "\n")
    try:
        moda = statistics.mode(result)
        f.write("Moda: " + str(moda) + "\n")
    except statistics.StatisticsError:
        f.write("Existe mas de un valor que podría ser la moda.\n")
    mediana = statistics.median(result)
    f.write("Mediana: " + str(mediana) + "\n")

    f.write("Distancias obtenidas:\nD = [")

    f.write(", ".join(map(str, result[0:10])))
    for i in range(20,300,10):
        f.write("\n     " + ", ".join(map(str, result[i-10:i])))

    f.write("]\n")

    f.close()

