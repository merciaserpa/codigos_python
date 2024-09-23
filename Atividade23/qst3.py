import time

# Solicitar ao usuário o número de segundos para a contagem regressiva
segundos = int(input("Digite o número de segundos para a contagem regressiva: "))

# Realizar a contagem regressiva
for contador in range(segundos, 0, -1):
    print(contador)
    time.sleep(1)  # Pausa de 1 segundo

# Mensagem final
print("Tempo esgotado!")