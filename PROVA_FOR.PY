#  Você está desenvolvendo um programa em Python para calcular a soma dos números pares 
# dentro de um intervalo determinado pelo usuário. 
# O programa deve solicitar ao usuário que insira dois números inteiros, 
# representando o início e o fim do intervalo (inclusive).
# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar 
# apenas os números pares. 
# Implemente a estrutura 'else' para exibir uma mensagem indicando que não há 
# números pares no intervalo, 
# caso seja o caso.

# Ao final, exiba a soma dos números pares encontrados.




inicio = int(input("informe o numero de inicio de intervalo: "))
fim = int(input("informe o numero do fim do intervalo: "))
soma = 0

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma += numero
if soma > 0:
    print(f"a soma dos numeros pares: {soma}")
else:
    print("nao tem numeros pares no intervalo.")

