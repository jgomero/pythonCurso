try:
    divisor = int(input("Ingresa un numero divisor: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e:#para guardar el error en una variable y mostrarlo luego
    print("Error: El divisor no puede ser cero")
    print("Ha ocurrido un error: ", e)
except ValueError as e: #para guardar el error en una variable y mostrarlo luego
    print("Error: Debes introducir un numero valido")
    print("Ha ocurrido un error: ", e)