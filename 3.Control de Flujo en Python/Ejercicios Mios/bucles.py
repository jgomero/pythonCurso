numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    print(i)

for i in range(10):
    print(i)

fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]

for fruta in fruits:
    print(fruta)
    if fruta == "Naranja":
        print("Naranja encontrada")

x = 0
while x < 5:
    print(x)
    x = x + 1

x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x = x + 1

numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    if i == 3:
        continue
    print(i)