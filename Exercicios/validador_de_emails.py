email_valido = True
print("Bem vindo(a) crie sua conta")
email = input("digite seu email").lower().strip()
if (email.count("@") == 0 or email.count("@") >= 2):
    email_valido = False
if email_valido == False:
       print("Email invalido")
else:
 print("Email valido")