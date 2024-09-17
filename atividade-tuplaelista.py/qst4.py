lista = []
for contador in range(10):
    numero = int(input("Informe um número inteiro: "))
    lista.append(numero)

posicao = 1
for numero in lista:
    if numero == 3:
        print(f"O número 3 está na posição {posicao}.")
    posicao += 1