#Ejemplo de iterador

#Crear una lista
my_list = [1, 2, 3, 4]

#Obtener el iterador
my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#Iteracion de strings

text = "Hola mundo"
#Creando el iterador
iter_text = iter(text)

#Iterar en la cadena
for char in iter_text:
    print(char)

#Iterando impares

#Limite
limit = 10

#Crear iterador
add_itter = iter(range(1,limit+1,2))

#usar el iterador
for num in add_itter:
    print(num)