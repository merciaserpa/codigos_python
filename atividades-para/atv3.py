numero = int(input("Digite um número: "))

# Encontrar divisores
for contador in range(1, (numero) + 1):
    if numero % contador == 0:
        print(contador)