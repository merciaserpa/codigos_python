import random

def gerar_numeros_aleatorios(inicio, fim):
    #Gera um número aleatório entre inicio e fim.
    return random.randint(inicio, fim)

numeros_gerados = []

for contador in range(5):
    # Solicita os limites ao usuário
    inicio = int(input("Digite o limite inferior: "))
    fim = int(input("Digite o limite superior: "))
    
    # Verifica se o limite inferior é menor que o superior
    if inicio <= fim:
        # Gera o número aleatório e armazena na lista
        numero_aleatorio = gerar_numeros_aleatorios(inicio, fim)
        numeros_gerados.append(numero_aleatorio)
        print(f"Número aleatório gerado: {numero_aleatorio}")
    else:
        print("O limite inferior deve ser menor que o limite superior. Tente novamente.")

# Exibe todos os números gerados
print("Números gerados:", numeros_gerados)