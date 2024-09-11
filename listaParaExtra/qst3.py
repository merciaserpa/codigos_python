# Definição da média para comparação
media = 33.5

# Inicialização dos contadores
acima_ou_igual_media = 0
abaixo_media = 0

# Recebe 7 temperaturas do usuário
for i in range(0,7):
    temperatura = float(input(f"Digite a {i+1} temperatura: "))

    # Conta quantas temperaturas estão acima ou iguais à média e abaixo da média
    if temperatura >= media:
        acima_ou_igual_media += 1
    else:
        abaixo_media += 1

# Exibe os resultados
print(f"Quantidade de temperaturas iguais ou acima da média ({media}): {acima_ou_igual_media}")
print(f"Quantidade de temperaturas abaixo da média ({media}): {abaixo_media}")