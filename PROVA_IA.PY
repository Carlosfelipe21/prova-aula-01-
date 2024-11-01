

# [LPIA-A05]Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. 
# O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas.
# Utilize um loop 'for' para iterar sobre os alunos e suas notas.
# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, 
# considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.
# Ao final, exiba a média geral da turma.






quantidade_aluno = int(input("Informe a quantidade de alunos: "))
soma_media = 0

for i in range(quantidade_aluno):
    nome = input(f"digite o nome do aluno{i+1}:")

    nota_01 = float(input("informe a primeira nota: "))
    nota_02 = float(input("informe a segunda nota: "))
    nota_03 = float(input("informe a terceira nota: "))

    media = (nota_01 + nota_02 + nota_03) /3
    soma_media += media

    if media >= 7.0:
        status = "Você foi APROVADO."
    else:
        status = "você foi REPROVADO."

    print(f"aluno: {nome}")
    print(f"notas: {nota_01}, {nota_02}, {nota_03}")
    print(f"media: {media:.2f}")

media_da_turma = soma_media / quantidade_aluno
print(f"A media geral da turma foi: {media_da_turma}.")
