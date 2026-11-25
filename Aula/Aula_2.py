name = input("digite seu nome").replace("á", "a")
print(name)

email = "roblox.nuggets@gmail.com"
print(email.find("@"))
print(email.count("a"))
print(email.startswith("ro"))
print(email.endswith("nuggets"))

print(email[0:email.find("@")])

frase = "python é o MAIOR"
lista = frase.split()

print(lista)

frase = "nome,idade,cidade,formação,hobby"
lista = frase.split(",")

print(lista)

junto = "+".join(lista)
print(junto)