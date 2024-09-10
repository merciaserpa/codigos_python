# Solicita ao usuário que insira o salário
salario = float(input("Digite o salário do funcionário: R$ "))

# Calcula o imposto com base nas faixas salariais
if salario <= 1900:
    imposto = 0
elif salario <= 2800:
    imposto = salario * 0.075
elif salario <= 3700:
    imposto = salario * 0.15
else:
    imposto = salario * 0.225

# Exibe o valor do imposto
print(f"O imposto a ser pago é: R$ {imposto:.2f}")