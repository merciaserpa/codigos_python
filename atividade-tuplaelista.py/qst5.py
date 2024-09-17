numeros = []
for num in range(5):
    numero = int(input(f"Informe o {num + 1}º número: "))
    numeros.append(numero)

print("Lista:", numeros)

for div_3 in numeros:
    if div_3 % 3 == 0:
        print("Números divisíveis por 3:", div_3)