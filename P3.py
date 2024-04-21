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
