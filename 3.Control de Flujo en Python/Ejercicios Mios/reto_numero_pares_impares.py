def numeros_pares(limit):
    a = 2
    while  a < limit:
        yield a
        a = a + 2
for num_par in numeros_pares(11):
    print(num_par)


def numeros_impares(limit):
    b = 1
    while  b < limit:
        yield b
        b = b + 2
for num_impar in numeros_impares(11):
    print(num_impar)


def generador_numeros():
    yield 1
    yield 2
    yield 3

mi_generador = generador_numeros()  # Crea un generador

print(next(mi_generador))  # 1
print(next(mi_generador))  # 2
print(next(mi_generador))  # 3
print(next(mi_generador))  # StopIteration (Error)


    