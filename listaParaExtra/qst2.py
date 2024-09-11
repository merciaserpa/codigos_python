# Contadores
negativos = 0
soma_positivos = 0

# Receber 8 números do usuário
for i in range(8):
    numero = int(input(f"Digite o {i+1} número: "))
    
    if numero < 0:
        negativos += 1
    else:
        soma_positivos += numero

# Exibir os resultados
print(f"Quantidade de números negativos: {negativos}")
print(f"Soma dos números positivos: {soma_positivos}")