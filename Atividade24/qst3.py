# Inicializa uma lista vazia para armazenar os eventos
eventos = []


def adicionar_evento():
    evento = input("Digite um novo evento: ")
    eventos.append(evento)
    print(f"Evento '{evento}' adicionado com sucesso!")


def remover_evento():
    evento = input("Digite o evento a ser removido: ")
    if evento in eventos:
        eventos.remove(evento)
        print(f"Evento '{evento}' removido com sucesso!")
    else:
        print(f"Evento '{evento}' não encontrado!")


def main():
    while True:
        print("\nEventos atuais:")
        if eventos:
            for i in range(len(eventos)):
                print(f"{i + 1}. {eventos[i]}")
        else:
            print("Nenhum evento encontrado.")

        print("\nOpções:")
        print("1. Adicionar um novo evento")
        print("2. Remover um evento")
        print("3. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            adicionar_evento()
        elif escolha == "2":
            remover_evento()
        elif escolha == "3":
            break
        else:
            print("Escolha inválida. Por favor, tente novamente!")

    print("Até logo!")

if __name__ == "__main__":
    main()