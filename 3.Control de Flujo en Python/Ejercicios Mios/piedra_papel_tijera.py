valores_permitidos = ["piedra", "papel", "tijera"]
player_1 = input("PLAYER 1, Ingresa Piedra/Papel/Tijera ")
player_2 = input("PLAYER 2, Ingresa Piedra/Papel/Tijera ")

while player_1 not in valores_permitidos:
    player_1 = input("PLAYER 1, Por favor solo Ingresa Piedra/Papel/Tijera ")

while player_2 not in valores_permitidos:
    player_1 = input("PLAYER 2, Por favor solo Ingresa Piedra/Papel/Tijera ")


if player_1 == player_2:
       print("Empataron")
elif player_1 == "piedra" and player_2 == "tijera":
        print("Gano Player 1")
elif player_1 == "papel" and player_2 == "piedra":
        print("Gano Player 1")
elif player_1 == "tijera" and player_2 == "papel":
        print("Gano Player 1")
else:
        print("Gano Player 2")



