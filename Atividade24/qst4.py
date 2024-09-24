animais = ['leão', 'tigre', 'elefante', 'girafa', 'zebra', 'macaco', 'panda', 'hipopotamo', 'leopardo', 'canguru', 'urso', 'coelho', 'cavalo', 'pinguim', 'lobo']

palavras_embaralhadas = [animais[(i * 3) % 15] for i in range(15)]
indice_aleatorio = 7
palavra_aleatoria = palavras_embaralhadas[indice_aleatorio]

tentativas = 3
while tentativas > 0:
    resposta = input(f"Em qual posição se encontra a palavra '{palavra_aleatoria}'? ")
    try:
        resposta = int(resposta)
        if resposta == indice_aleatorio:
            print("Parabéns! Você acertou!")
            break
        else:
            tentativas = tentativas - 1
            print(f"Você errou! Restam {tentativas} tentativas.")
    except ValueError:
        print("Resposta inválida. Por favor, digite um número entre 0 e 14.")

if tentativas == 0:
    print(f"A palavra '{palavra_aleatoria}' se encontra na posição {indice_aleatorio}.")

print("A lista de palavras embaralhada é:")
print(palavras_embaralhadas)