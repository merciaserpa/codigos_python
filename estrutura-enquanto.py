#1ª forma de utilizar while - semelhante ao FOR

contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1 # é o mesmo quecontador +=1
    
print("="*40)
#2ª forma de utilizar enquanto - loop condicional normal
valor = 0

while valor >= 0:
    valor = int(input("Informe um valor qualquer(digite um valor negativo para terminar:)"))
    
    print(f"Você digitou{valor}")
    
print("="*40)

#3ª forma de utilizar o enquanto - semelhante a estrutura faça..enquanto

while True:
    senha = input("Informe sua senha: ")
    if senha == "123":
        print("Parabéns, senha correta")
        break # forma de  encerrar o loop
    else:
        print("Senhas não conferem, tente novamente")