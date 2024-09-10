# Solicita a nota final e a frequência do aluno
nota_final = float(input("Digite a nota final do aluno: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

# Inicializa a variável de aprovação
aprovado = False

# Verifica se a nota é maior ou igual a 7
if nota_final >= 7:
    # Se a nota for suficiente, verifica se a frequência é maior ou igual a 75%
    if frequencia >= 75:
        aprovado = True

# Exibe o resultado com base na variável de aprovação
if aprovado:
    print("O aluno está aprovado.")
else:
    print("O aluno está reprovado.")