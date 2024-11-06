# [LPIA-A06]  Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. 
# Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. 
# Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.

# Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.


usuario_correto = "felipe21"
senha_correta = "#felipe21"

numero_tentativas = 3

for tentativa in range(numero_tentativas):
    usuario = input("informe seu nome de usuario: ")
    senha = input("informe sua senha de acesso: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Ola, seja muito bem vindo!")
        break
    else:
        numero_tentativas -= 1
        if numero_tentativas > 0:
            print(f"Credenciais incorretas. voce tem {numero_tentativas} tentativas.")
        else:
            for _ in range(3):
                print("Seu acesso foi BLOQUEADO.")