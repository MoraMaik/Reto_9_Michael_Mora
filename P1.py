import math

# Lambda para saludar
saludar = lambda: print("¡Hola Profe Felipe! Aqui puedes mirar lo que hice con el reto 9.")

# Lambda para calcular el area de un rectángulo
calcular_area_rectangulo = lambda ancho, alto: ancho * alto

# Lambda para elevar un numero al cuadrado
elevar_cuadrado = lambda numero: math.pow(numero, 2)

# Lambda para sumar dos numeros
sumar_dos_numeros = lambda num1, num2: num1 + num2

def main():
    # Funcion principal del programa
    saludar()

    # Demostracion de calculo del area de un rectangulo
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    alto = float(input("Ingrese el alto del rectángulo: "))
    area_rectangulo = calcular_area_rectangulo(ancho, alto)
    print("El área del rectángulo es:", area_rectangulo)

    # Demostracion de elevar un numero al cuadrado
    numero = float(input("Ingrese un número para elevar al cuadrado: "))
    cuadrado = elevar_cuadrado(numero)
    print("El número elevado al cuadrado es:", cuadrado)

    # Demostracion de sumar dos numeros
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    suma = sumar_dos_numeros(num1, num2)
    print("La suma de los dos numeros es:", suma)

if __name__ == "__main__":
    main()
