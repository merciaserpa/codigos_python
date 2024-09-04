# Ler os valores inteiros A e B
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Verificar se A é divisível por B
if B != 0 and A % B == 0:
    print("O valor de A é divisível por B")
else:
    print("O valor de A não é divisível por B")