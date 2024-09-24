def main():
    notas = []


    while True:
        nota = float(input("Digite a nota do aluno (ou 0 para terminar): "))
        if nota == 0:
            break
        notas.append(nota)

    media = 7
    alunos_acima_media = 0

    for nota in notas:
        if nota > media:
            alunos_acima_media += 1

    print(f"Quantidade de alunos com notas acima da média: {alunos_acima_media}")

if __name__ == "__main__":
    main()