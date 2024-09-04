# Ler os valores inteiros A e B
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Verificar se os valores são iguais
if A == B:
    C = A + B  # Se forem iguais, somar os dois
else:
    C = A * B  # Se forem diferentes, multiplicar A por B

# Exibir o resultado
print(f"O valor de C é: {C}")