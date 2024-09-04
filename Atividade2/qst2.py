# Ler os dados da pessoa
nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo (M/F): ")
estado_civil = input("Digite o seu estado civil (SOLTEIRA, CASADA, DIVORCIADA, VIÚVA): ")

# Verificar se o sexo é "F" e o estado civil é "CASADA"
if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = input("Digite o tempo de casada (em anos): ")
    print(f"{nome}, você está casada há {tempo_casada} anos.")
else:
    print(f"{nome}, obrigado e até a próxima.")