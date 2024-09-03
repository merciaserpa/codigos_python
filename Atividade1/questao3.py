# Leitura do nome da fazenda
nome_fazenda = input("Digite o nome da fazenda: ")

# Leitura da quantidade de cavalos
quantidade_cavalos = int(input("Digite a quantidade de cavalos na fazenda: "))

# Cada cavalo precisa de 4 ferraduras
ferraduras_necessarias = quantidade_cavalos * 4

# Exibição do resultado
print(f"Fazenda: {nome_fazenda}")
print(f"Quantidade de cavalos: {quantidade_cavalos}")
print(f"Quantidade de ferraduras necessárias: {ferraduras_necessarias}")
