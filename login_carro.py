login = []

carros = ["Peugeot 2009", ]

conta = {
    "nome": input("digite um nome: "),
    "senha": input("digite uma senha: "),
}

print("faça login na sua conta\n______________________")

login = {
    "nome": input("digite seu nome: "),
    "senha": input("digite sua senha: "),
}

while login['senha'] != conta['senha']:
    nome = input("_______________\ndigite seu nome novamente: ")
    senha = input("digite sua senha novamente: ")
    if senha == conta['senha']:
        break
        
print("login feito com sucesso")

         