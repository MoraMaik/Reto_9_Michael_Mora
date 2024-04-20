# Reto_9_Michael_Mora
Desarrollo reto 9, segun lo aprendido en clase de Funciones 2.
_______________________________
## **Punto 1**

**Instrucciones:** De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
```python
import math

# Lambda para saludar
saludar = lambda: print("¡Hola Profe Felipe! Aqui puedes mirar lo que hice con el reto 9.")

# Lambda para calcular el area de un rectangulo
calcular_area_rectangulo = lambda ancho, alto: ancho * alto

# Lambda para elevar un numero al cuadrado
elevar_cuadrado = lambda numero: math.pow(numero, 2)

# Lambda para sumar dos numeros
sumar_dos_numeros = lambda num1, num2: num1 + num2

def main():
    # Funcion principal del programa
    saludar()

    # Demostracion de calculo del area de un rectangulo
    ancho = float(input("Ingrese el ancho del rectangulo: "))
    alto = float(input("Ingrese el alto del rectangulo: "))
    area_rectangulo = calcular_area_rectangulo(ancho, alto)
    print("El area del rectangulo es:", area_rectangulo)

    # Demostracion de elevar un numero al cuadrado
    numero = float(input("Ingrese un numero para elevar al cuadrado: "))
    cuadrado = elevar_cuadrado(numero)
    print("El numero elevado al cuadrado es:", cuadrado)

    # Demostracion de sumar dos numeros
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    suma = sumar_dos_numeros(num1, num2)
    print("La suma de los dos numeros es:", suma)

if __name__ == "__main__":
    main()
```
En este punto, opte por seleccionar algunas funciones de cada reto y clases anteriores. Puesto que cada ejercicio debe contar con su propio programa, estas funciones reescritas como expresiones lambda se ejecutaran secuencialmente.

_______________________________
## **Punto 2**

**Instrucciones:** De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
```python
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
```
* las funciones utilizadas fueron:

1. Calcular mediana de varios conjuntos de numeros
Esta funcion acepta varios conjuntos de numeros (cada conjunto siendo una lista) y calculara la mediana para cada conjunto.

2. Verificar si multiples numeros son primos
La funcion se ajusta para aceptar multiples numeros y verificar la primalidad de cada uno.

3. Calcular el factorial de varios numeros
Similarmente, esta funcion puede ahora tomar varios numeros y calcular el factorial de cada uno.
