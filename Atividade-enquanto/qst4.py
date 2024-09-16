# Início do programa
print("Lojão do Manoel")

total_compra = 0.0
contador_produtos = 1

while True:
    preco = float(input(f"Produto {contador_produtos}: R$ "))
    
    if preco == 0:
        break
    
    total_compra += preco
    contador_produtos += 1

print(f"Total: R$ {total_compra:.2f}")

dinheiro = float(input("Dinheiro: R$ "))
troco = dinheiro - total_compra

print(f"Troco: R$ {troco:.2f}")

