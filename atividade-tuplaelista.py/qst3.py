numeros = []
for contador in range(6):
    numeros.append(float(input("Informe um número: ")))
    
print("lista de números: ", numeros)

posicao1, posicao2 = int(input("Informe a primeira posição: ")), int(input("Informe a segunda posição: "))

numero1, numero2 = numeros[posicao1], numeros[posicao2]

operacoes = (numero1 * numero2, numero1 + numero2, numero1 - numero2, numero1 / numero2, numero1 ** numero2)

print(f"Operações: ")
print(f"Produto: {operacoes[0]}")
print(f"Soma: {operacoes[1]}")
print(f"Diferença: {operacoes[2]}")
print(f"Divisão : {operacoes[3]}")
print(f"Exponenciação: {operacoes[4]}")