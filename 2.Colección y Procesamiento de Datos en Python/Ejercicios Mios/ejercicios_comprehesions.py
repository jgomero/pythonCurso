#DOBLE NUMERO

numbers = [1, 2, 3, 4, 5]
double_number = [x*2 for x in numbers]

print(double_number)

#FILTRAR Y TRANSFORMAR EN UN SOLO PASO

words = ["sol", "mar", "montana", "rio", "estrella"]
words_modified = [x.upper() for x in words if len(x) > 3]
print(words_modified)

#CREAR UN DICCIONARIO CON LIST COMPREHENSION

claves = ["nombre", "edad", "ocupacion"]
valores = ["Juan", 30, "Ingeniero"]

diccionario = {claves[i] : valores[i] for i in range(len(claves))}
print(diccionario)

#ANIDACION DE LIST COMPREHENSIONS
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_transpuesta = [[row[i] for row in matriz] for i in range(len(matriz[0]))]
print(matriz_transpuesta)

#EXTRAER INFORMACION DE UNA LISTA DE DICCIOANARIOS

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
peronas_filter = [x["nombre"] for x in personas if x["ciudad"] == "Madrid" and x["edad"] > 30]
print(peronas_filter)


#LIST COMPREHENSION CON UN ELSE
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_modificados = [x*2 if x%2 == 0 else x for x in numeros]
print(numeros_modificados)