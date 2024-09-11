# Solicita ao usuário os dois números inteiros positivos
a = int(input("Digite o primeiro número inteiro positivo: "))
b = int(input("Digite o segundo número inteiro positivo: "))

# Inicializa a variável para armazenar o total
total_multiplos = 0

# Percorre os números entre a e b
for i in range(a, b + 1):
    if i % 7 == 0 and i % 11 == 0:
        total_multiplos += 1

# Exibe o resultado final
print(f"O total de números entre {a} e {b} que são múltiplos de 7 e 11 é: {total_multiplos}")