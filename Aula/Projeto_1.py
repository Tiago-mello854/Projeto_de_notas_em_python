from shlex import join

frase = input("digite uma frase: ")
count = 1
lista = frase.split()
for world in lista:
    print(f"{count} - {world}" , end="---> ")
    print(world[::-1])
    count = count + 1
    invertlist = lista [::-1]
    print(", ".join(invertlist))
