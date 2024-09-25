def exibir_cardapio(cardapio): 
    print("\nCardápio:") #Exibe o cardápio completo
    for prato, preco in cardapio.items():
        print(f"{prato}: R$ {preco:.2f}")

cardapio = {} # Dicionário para armazenar o cardápio

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar prato")
    print("2. Remover prato")
    print("3. Consultar preço de um prato")
    print("4. Exibir cardápio completo")
    print("5. Sair")
    
    opcao = input("\nDigite o número da opção desejada: ")
    
    if opcao == '1':
        prato = input("Informe o nome do prato a ser adicionado: ")
        preco = float(input("Informe o preço do prato: R$ "))
        cardapio[prato] = preco
        print(f"\n-Prato {prato} adicionado com sucesso!")
    
    elif opcao == '2':
        prato = input("Digite o nome do prato a ser removido: ")
        if prato in cardapio:
            del cardapio[prato]
            print(f"\n-Prato {prato} removido com sucesso!")
        else:
            print(f"\n-Prato {prato} não encontrado no cardápio")
    
    elif opcao == '3':
        prato = input("Digite o nome do prato para consultar o preço: ")
        if prato in cardapio:
            print(f"\n-O preço de {prato} é R$ {cardapio[prato]:.2f}")
        else:
            print(f"\n-Prato {prato} não encontrado no cardápio")
    
    elif opcao == '4':
        exibir_cardapio(cardapio)
    
    elif opcao == '5':
        print("\n-Saindo do programa\n")
        break
    
    else:
        print("\n-Opção inválida!")