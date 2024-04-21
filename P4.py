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
