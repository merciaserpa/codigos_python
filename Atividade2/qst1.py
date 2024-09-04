# Ler os valores A, B e C
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

# Verificar se a soma de A e B é menor que C
if A + B < C:
    print(f"A soma de {A} e {B} é menor que {C}.")
else:
    print(f"A soma de {A} e {B} não é menor que {C}.")