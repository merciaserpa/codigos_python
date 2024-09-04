valor = float(input("Informe o valor: "))
metodo = int(input("informe o metodo de pagamento: 1-PIX, 2-Cartão á vista , 3- Cartão 2vezes , 4- Cartão 3vezes "))

if metodo==1:
    desconto= valor*0.15
    final = valor-desconto
    print(f"valor a ser pago é de {final:.2f} reais" )
elif metodo==2:
    desconto= valor*0.10
    final = valor-desconto
    print(f"valor a ser pago é de {final:.2f} reais")
elif metodo==3:
    print(f"valor a ser pago é de {valor:.2f} reais")

elif metodo==4:
    desconto= valor*0.10
    final = valor+desconto
    print(f"valor a ser pago é de {final :.2f} reais")

else:
    print("metodo de pagamento não selecionado")
