# Inicializar o contador para pessoas com 18 anos ou mais
idade_18 = 0

# Solicitar a idade de 5 pessoas
for idade in range(1,6):
    idadee = int(input(f"Digite a idade da pessoa {idade}: "))
    
# Verificar se a idade é maior ou igual a 18
    if idadee >= 18:
        idade_18 += 1

print(f"A quantidade de pessoas com 18 anos ou mais é: {idade_18}")