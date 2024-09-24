eventos = []

def adicionar_evento():
    evento = input("Digite o nome do evento: ")
    eventos.append(evento)
    print("Evento adicionado com sucesso!")

def remover_evento():
    evento = input("Digite o nome do evento: ")
    if evento in eventos:
        eventos.remove(evento)
        print("Evento removido com sucesso!")
    else:
        print("Evento não encontrado!")

def exibir_eventos():
    print("Eventos agendados:")
    for evento in eventos:
        print(evento)

while True:
    print("Agendador de Eventos")
    print("1. Adicionar novo evento")
    print("2. Remover evento existente")
    print("3. Sair")
    opcao = input("Digite a opção: ")

    if opcao == "1":
        adicionar_evento()
    elif opcao == "2":
        remover_evento()
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")