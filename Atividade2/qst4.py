# Ler o valor do usuário
valor = int(input("Digite um valor: "))

# Verificar se o valor é par ou ímpar
if valor % 2 == 0:
    resultado = valor + 10  # Se o valor for par, somar 10
else:
    resultado = valor * 2   # Se o valor for ímpar, multiplicar por 2

# Exibir o resultado
print(f"O resultado da operação é: {resultado}")