# Cotações fixas
cotacoes = {
    "Dólar": 5.48,
    "Euro": 6.10,
    "Libra": 7.30,
    "Peso Argentino": 0.0057,
    "Iene": 0.038,
}

valor_reais = float(input("Digite o valor em reais: "))
moeda = input("Informe a moeda (Dólar, Euro, Libra, Peso Argentino, Iene): ")

# Converte o valor para a moeda escolhida
if moeda in cotacoes:
    valor_convertido = valor_reais / cotacoes[moeda]
    print(f"{valor_reais} reais equivalem a {valor_convertido:.2f} {moeda}.")
else:
    print("Moeda inválida.")