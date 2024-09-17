numeros = []

while True:
  valor = int(input("informe um número (ou um valor negativo para encerrar): "))
  if valor < 0:
    break
  else:
     numeros.append(valor) # Adiciona o valor à lista
   
# Exibe a lista criada
print("Lista criada:", numeros)

for contador in numeros:
    if contador % 2 == 0:
        numeros.remove(contador)
        print(numeros)