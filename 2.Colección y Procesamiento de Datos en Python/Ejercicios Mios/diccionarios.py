numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers)

#DICCIONARIO EJEMPLO

information = {"nombre": "Jose",
               "Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29}
print(information)
del information["Edad"]
print(information)

#METODOS DE DICCIONARIO

#KEYS
claves = information.keys()
print(claves)
print(type(claves))

#VALUES
values = information.values()
print(values)
print(type(values))

#ITEMS
pairs = information.items()
print(pairs)
print(type(pairs))

#EJEMPLO CREANDO UNA AGENDA DE CONTACTOS

contacts = {"Jose": {"Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29},

               "Luis": {"Apellido": "Boston",
               "Altura": 1.90,
               "Edad": 23},}
print(contacts)
print(contacts["Luis"])