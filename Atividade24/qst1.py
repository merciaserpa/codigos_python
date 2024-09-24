def main():
    lista1_input = input("Digite os números inteiros da primeira lista, separados por espaço: ")
    lista1 = []
    for num in lista1_input.split():
        lista1.append(int(num))

    lista2_input = input("Digite os números inteiros da segunda lista, separados por espaço: ")
    lista2 = []
    for num in lista2_input.split():
        lista2.append(int(num))

    # Encontrar a interseção
    intersecao = []
    for num in lista1:
        if num in lista2 and num not in intersecao:
            intersecao.append(num)

    for i in range(len(intersecao)):
        for j in range(i + 1, len(intersecao)):
            if intersecao[i] > intersecao[j]:
                intersecao[i], intersecao[j] = intersecao[j], intersecao[i]


    print("Números comuns (interseção):", intersecao)

if __name__ == "__main__":
    main()