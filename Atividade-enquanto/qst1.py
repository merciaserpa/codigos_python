while True:
  numero = int(input("Digite um número inteiro: "))
  if numero < 0:
    break
  elif numero > 100:
    print("Limite excedido")
  elif numero > 10:
    print(numero**2)
  elif numero > 5:
    print(numero**3)