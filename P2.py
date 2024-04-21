def calcular_mediana(*args):
    # Lista para almacenar las medianas de cada conjunto de numeros
    resultados = []
    # Itera sobre cada conjunto de numeros proporcionado
    for numeros in args:
        # Ordena los numeros del conjunto actual
        numeros_ordenados = sorted(numeros)
        # Calcula el tamaño de la lista ordenada
        n = len(numeros_ordenados)
        # Determina el indice del elemento medio
        medio = n // 2
        # Si la lista tiene un numro par de elementos, calcula la mediana como el promedio de los dos elementos centrales
        if n % 2 == 0:
            resultados.append((numeros_ordenados[medio - 1] + numeros_ordenados[medio]) / 2)
        # Si la lita tiene un numero impar de elementos, la mediana es el elemento central
        else:
            resultados.append(numeros_ordenados[medio])
    return resultados

def es_primo(*args):
    # Lista para almacenar los resultdos booleanos de la primalidad
    resultados = []
    # Itera sobre cada numero proporcionado
    for numero in args:
        # Un numero debe ser mayor que 1 para ser primo
        if numero < 2:
            resultados.append(False)
            continue
        # Asume que el numero es primo hasta que se demuestre lo contrario
        is_prime = True
        # Comprueba los divisores hasta la raiz cuadrada del numero
        for divisor in range(2, int(numero**0.5) + 1):
            if numero % divisor == 0:
                is_prime = False
                break
        resultados.append(is_prime)
    return resultados

def calcular_factorial(*args):
    # Lista para almacenar los factoriales calculados
    resultados = []
    # Itera sobre cada numero proprcionado
    for numero in args:
        # El factorial de 0 es 1 por definicion
        if numero == 0:
            resultados.append(1)
            continue
        factorial = 1
        # Calcula el factorial multiplicando todos los numeros hasta el numero dado
        for i in range(1, numero + 1):
            factorial *= i
        resultados.append(factorial)
    return resultados

# Ejemplo de como se usa:
print(calcular_mediana([1, 3, 5], [2, 8, 10, 20]))  # Deberia mostrar las medianas de cada lista
print(es_primo(29, 15, 23))  # Deberia mostrar una lista de booleanos indicando si cada numero es primo
print(calcular_factorial(5, 4, 3))  # Deberia mostrar los factoriales de los numeros dados
