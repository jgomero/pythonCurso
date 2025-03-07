#obteniendo por un rango
squares = [x**2 for x in range(1,11)]
print("Cuadrados:", squares)

#obteniendo temperatura usando ya una lista hecha
celsius = [0, 10, 20, 30, 40]
celsius_range = [x for x in range(0, 41, 10)] #es un rango de 0 a 41 que aumenta de 10 en 10, no toma el 41
celsius_range2 = [x * 10 for x in range(5)] #genera un rango de 0 a 5, no toma en cuenta el 5
fahrenheit = [(temp * 9/5) * 32 for temp in celsius]
print("Temperatura en F:", fahrenheit)

#Numeros pares
evens = [x for x in range(1,21) if x%2 == 0]
print(evens)

#matrices
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)

#EJERCICIOS

#Doble de Numeros

