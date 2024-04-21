# Reto_9_Michael_Mora

Desarrollo reto 9, segun lo aprendido en clase de [Funciones 2](http://https://github.com/fegonzalez7/pdc_unal_clase12 "Funciones 2").
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

_______________________________
## **Punto 3**

**Instrucciones:** Escriba una funcion recursiva para calcular la operacion de la potencia.
```python
def potencia(base, exponente):

    # caso base: cualquier numero elevado a 0 es 1
    if exponente == 0:
        return 1
    
    # caso para exponente negativo: usar la propiedad de que a^-b = 1/a^b
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    
    # paso recursivo: multiplicar la base por la potencia de la base al exponente menos uno
    else:
        return base * potencia(base, exponente - 1)

# ejemplos de uso de la funion
    
print(potencia(2, 3))  # deberia indicar 8

print(potencia(5, 0))  # deberia indicar 1

print(potencia(2, -2))  # deberia indicar 0.25
```
+ **Caso base**: Cuando el exponente es 0 la funcion retorna 1 directamente, ya que cualquier numero elevado a 0 es 1.
+ **Exponente negativo**: Si el exponente es negativo, la funcion convierte el problema en uno de exponente positivo y luego toma el reciproco del resultado. Esto se hace llamando a la misma funcion con el exponente positivo equivalente (el negativo del exponente actual) y dividiendo 1 por el resultado de esa llamada recursiva.
+ **Paso recursivo**: Para los exponentes positivos, la funcion se llama a si misma con el exponente disminuido en uno hasta que se alcanza el caso base, multiplicando la base cada vez.

_______________________________
## **Punto 4**

**Instrucciones:** Utilice la siguiente plantilla de code para contar el tiempo:
```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecucion
end_time = time.time()

timer = end_time - start_time
print(timer)
```
Realice pruebas para calcular fibonacci con iteracion o con recursion. Determine desde que numero de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este [hilo](http://https://stackoverflow.com/questions/8220801/how-to-use-timeit-module "hilo") .

```python
import time

# funcion de Fibonacci usando recursion

def fibonacci_recursivo(n):
    if n <= 1:

        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# funcion de Fibonacci usando iteracion
def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# prueba de tiempo de la funcion recursiva
start_time = time.time()

# cambiar el valor de 'n' para realizar la prueba con diferentes numeros
fibonacci_recursivo(30)
end_time = time.time()
print("Tiempo de ejecucion recursivo:", end_time - start_time)

# prueba de tiempo de la funcion iterativa
start_time = time.time()

# cambiar el valor de 'n' para realizar la prueba con difrentes numeros
fibonacci_iterativo(30)
end_time = time.time()

print("Tiempo de ejecucion iterativo:", end_time - start_time)

```
Es importante destacar que la version recursiva tiene una complejidad temporal exponencial y puede ser muy lenta para valores grandes de `n`, mientras que la version iterativa tiene una complejidad lineal y es mucho mas rapida.

_______________________________
## **Punto 5**

**Instrucciones:** Crear cuenta en stackoverflow y adjuntar imagen en el repo

[![image.png](https://i.postimg.cc/y6b5bS03/image.png)](https://postimg.cc/jCyZW2gR)


Por alguna razon no deja expresarlo de manera mas simple, este es el link: https://stackoverflow.com/users/24527579/moramaik?tab=profile

_______________________________
## **Punto 6**

**Instrucciones:** Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que esten iniciando, si tienen tiempo para redes poco utiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalon. Dejar enlace en el repo.

[![image.png](https://i.postimg.cc/MpDmghg3/image.png)](https://postimg.cc/yDDRZr10)

[Link de mi perfil aqui](http://www.linkedin.com/in/michael-kaleth-mora-mejia-2571b2303 "Link de mi perfil aqui")

_______________________________
**FIN RETO**
