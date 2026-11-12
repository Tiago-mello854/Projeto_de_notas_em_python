pontos = 0
print("Pergunta de 1 a 5")
print("Quiz de minecraft")
print("Qual mob explode quando chega perto do jogador?")
resposta = input("digite a sua resposta: ").strip().lower()
if resposta == "creeper":
    print("correto")
    pontos += 1
else:
    print("incorreto")
print("Qual é o chefe que fica na dimensão do End?")
resposta = input("digite a sua resposta: ").strip().lower()
if resposta == "ender dragon":
    print("correto")
    pontos += 1
else:
    print("incorreto")
print("Qual material você usa para fazer uma mesa de trabalho?")
resposta = input("digite a sua resposta: ").strip().lower()
if resposta == "madeira":
    print("correto")
    pontos += 1
else:
 print("incorreto")
print("Qual item serve para ativar o portal do Nether?")
resposta = input("digite a sua resposta: ").strip().lower()
if resposta == "isqueiro":
    print("correto")
    pontos += 1
else:
 print("incorreto")
print("Qual mob consegue se teletransportar?")
resposta = input("digite a sua resposta: ").strip().lower()
if resposta == "enderman":
    print("correto")
    pontos += 1
else:
 print("incorreto")
if pontos == 5:
    print("Parabéns você acertou tudo")
else:
 print("você não acertou tudo, tudo bem boa sorte da proxima vez!")
print(f"Sua pontuação foi de: {pontos} pontos")