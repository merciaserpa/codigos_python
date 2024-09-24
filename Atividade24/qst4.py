import random

def jogo_palavras():

    palavras = [
        'leão', 'tigre', 'elefante', 'girafa', 'zebra',
        'maçã', 'banana', 'laranja', 'morango', 'uva',
        'Brasil', 'Canadá', 'Japão', 'Austrália', 'França'
    ]

    random.shuffle(palavras)

    # Escolher uma palavra aleatória da lista
    palavra_escolhida = random.choice(palavras)
    indice_correto = palavras.index(palavra_escolhida)

    # Inicializar o número de tentativas
    tentativas = 3

    print("Bem-vindo ao jogo das palavras!")
    print("A lista de palavras foi embaralhada e você não a verá novamente.")
    print("Você terá que adivinhar a posição de uma palavra escolhida aleatoriamente.")
    print("A lista começa na posição 0 e vai até 14.")
    print("Você tem 3 tentativas para acertar.")

    while tentativas > 0:
        try:
            # Exibir a palavra escolhida
            print(f"\nA palavra escolhida é: '{palavra_escolhida}'")
            palpite = int(input("Digite a posição da palavra: "))

            if palpite < 0 or palpite > 14:
                print("Posição inválida. Por favor, tente novamente.")
                continue

            if palpite == indice_correto:
                print("Parabéns! Você acertou!")
                break
            else:
                tentativas -= 1
                print(f"Desculpe, isso não está correto. Você tem {tentativas} tentativas restantes.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    if tentativas == 0:
        print(f"Desculpe, você não acertou. A posição correta é {indice_correto}.")
        print("Boa sorte na próxima vez!")

    print("\nA lista embaralhada é:")
    for i in range(len(palavras)):
        print(f"{i}. {palavras[i]}")

jogo_palavras()