turma = input("Digite o nome da turma: ")
quantidade_alunos = int(input("digite o número de alunos: "))
alunos = []
notas = []

for i in range(1, (quantidade_alunos + 1)):
    alunos.append(input(f"Digite o nome do aluno {i}: "))
    notas.append(int(input(f"Digite a nota do aluno {i}: ")))

print()

print(f"Estatísticas da {turma}:")
media = sum(notas) / quantidade_alunos
maior_nota = max(notas)
menor_nota = min(notas)

print()

print(f"Maior nota = {maior_nota}")
print(f"Menor nota = {menor_nota}")
print(f"Média de notas = {media}")
print()

for i in range(quantidade_alunos):
    if notas[i] < 5:
        print(f"{alunos[i]} tirou insuficiente")
    elif notas[i] >= 5 and notas[i] <=6 :
        print(f"{alunos[i]} tirou suficiente")
    elif notas[i] >= 7 and notas[i] <= 8:
        print(f"{alunos[i]} tirou bom")
    else:
        print(f"{alunos[i]} tirou muito bom")

print()

agrupados = zip(notas, alunos)
ordenados = []
for nota, aluno in sorted(agrupados, reverse=True):
    ordem = aluno, nota
    ordenados.append(ordem)
    print(f"{aluno}: {nota}")