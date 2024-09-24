import random

# Cria uma lista com os resultados possíveis
moeda = ["Cara", "Coroa"]
resultados = []

# Inicia o loop para lançar a moeda
continuar = 's'
while continuar == 's':
    # Lança a moeda
    resultado = random.choice(moeda)
    # Armazena o resultado
    resultados += [resultado]
    # Exibe o resultado
    print("Resultado do lançamento:", resultado)
    
    # Pergunta ao usuário se deseja lançar novamente
    continuar = input("Deseja lançar a moeda novamente? (s/n): ").strip().lower()

# Exibe todos os resultados
print("Resultados de todos os lançamentos:", resultados)