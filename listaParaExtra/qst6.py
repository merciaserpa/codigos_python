# Recebe um número inteiro do usuario
n = int(input("Digite um número inteiro: "))

# Inicializa a variável para a soma dos divisores próprios
soma_divisores = 0

# Encontra e soma os divisores próprios positivos de n
for i in range(1, n):
    if n % i == 0:  # Verifica se i é um divisor de n
        soma_divisores += i

# Verifica se a soma dos divisores próprios é igual ao número
if soma_divisores == n:
    print(f"{n} é um número perfeito.")
else:
    print(f"{n} não é um número perfeito.")