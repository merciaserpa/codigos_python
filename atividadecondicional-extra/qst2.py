# Solicita ao usuário que insira um ano
ano = int(input("Digite um ano: "))

#Verificar se o ano é bissexto
if ano % 400 == 0:
    print(f"O ano {ano} é bissexto.")
else:
    if ano % 4 == 0:
        if ano % 100 != 0:
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")