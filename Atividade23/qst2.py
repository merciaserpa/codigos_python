# Solicitar ao usuário o valor da conta e o percentual de gorjeta
valor_conta = float(input("Digite o valor da conta em R$: "))
percentual_gorjeta = float(input("Digite o percentual de gorjeta (por exemplo, 10, 15 ou 20): "))

# Calcular o valor da gorjeta
gorjeta = (percentual_gorjeta / 100) * valor_conta

# Calcular o total da conta com a gorjeta incluída
total = valor_conta + gorjeta

# Exibir os resultados
print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total: R$ {total:.2f}")
