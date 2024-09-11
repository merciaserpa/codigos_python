import random

# Inicializa a lista para contar as ocorrências de cada valor
contagem = [0] * 6

# Simula o lançamento de dados 10 vezes
for _ in range(10):
    lancamento = random.randint(1, 6)
    contagem[lancamento - 1] += 1

# Exibe a contagem de cada valor
for i in range(6):
    print(f"Valor {i + 1}: {contagem[i]} vezes")

