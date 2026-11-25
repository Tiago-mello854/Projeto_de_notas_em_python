agenda = {"tiago":912312312, "andre":1293129312}
while True:

    agenda["nome"] = input("digite o seu nome:")
    agenda["numero"] = int(input("digite o seu número:"))
    sair = input("deseja sair? [S/N]").upper()
    if sair == "S":
        break
while True:
    pesquisar = input("digite o nome que você quer pesquisar:")
    if pesquisar == "sair":
        break
    elif pesquisar in agenda:
        print(f"o telefone do(a){agenda[pesquisar]}")
    else:
        print("contato não encontrado")