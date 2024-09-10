# Solicita ao usuário a quantidade de horas trabalhadas e o valor por hora
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: R$ "))

# Define o limite de horas normais e o percentual de bônus para horas extras
limite_horas_normais = 40
bonus_percentual = 0.50

# Calcula o salário
if horas_trabalhadas > limite_horas_normais:
    horas_normais = limite_horas_normais
    horas_extras = horas_trabalhadas - limite_horas_normais
    salario = (horas_normais * valor_por_hora) + (horas_extras * valor_por_hora * (1 + bonus_percentual))
else:
    salario = horas_trabalhadas * valor_por_hora

# Exibe o salário total
print(f"O salário total a receber é: R$ {salario:.2f}")