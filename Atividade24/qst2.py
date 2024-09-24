
notas = []
soma_notas = 0
contador_alunos = 0
while True:
    nota = float(input("Digite a nota do aluno (ou 0 para terminar): "))
    if nota == 0:
        break
    notas.append(nota)
    soma_notas += nota
    contador_alunos += 1

media = soma_notas / contador_alunos
print("Média da turma:", media)

acima_media = [nota for nota in notas if nota > media]
contador_acima_media = 0
for nota in acima_media:
    contador_acima_media += 1
print("Quantidade de alunos com nota acima da média:", contador_acima_media)