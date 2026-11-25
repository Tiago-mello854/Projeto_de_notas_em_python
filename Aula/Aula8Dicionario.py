personagem = {
    "nome":"kratos",
    "level":50,
    "xp":250,
    "mestria":99,
    "atk":150,
    "def":200
}

print(personagem["level"])
print(personagem)

print("personagem")
for k, v in personagem.items():
    print(f"{k}: {v}")

    jogador = {}
    jogador["nome"] = input("Digite o nome do jogador: ")
    jogador["level"] = int(input("Digite o level do jogador: "))
    jogador["xp"] = int(input("Digite o xp do jogador: "))
    jogador["mestria"] = int(input("Digite a mestria do jogador: "))
    jogador["atk"] = int(input("Digite o ataque do jogador: "))
    jogador["def"] = int(input("Digite a defesa do jogador: "))

    print(jogador)
    for k, v in jogador.items():
        print(f"{k}: {v}")