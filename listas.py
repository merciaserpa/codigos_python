animais = ["Cachorro","Gato","Ovelha"]
print(type(animais))#exibindo o tipo de variável

print(animais)

#Exibindo todos os itens da lista 
print("-"*50)
for itens in animais:
    print(itens)
    
#1ª Etapa: Atualizar dados
print("-"*50)
animais[0] = "Coelho"
print(animais)

#2ª Etapa: Inserir dados
print("-"*50)
#Forma 1 - Usando append 
animais.append("Cavalo")#irá inserir um novo item no final da lista
print(animais)

#2ª Forma - Usando Insert
animais.insert(1, "Pássaro")# o insert precisa de dois valores, o 1º será o índice que sejo inserir o valor. O 2º é o conteúdo que quero inserir na lista
print(animais)

#3ª Etapa:Excluir dados
print("-"*50)
#Forma 1 - usando pop()
animais.pop()#Remove o último item da lista
print(animais)

#Forma 2 - Usando pop() com índice
animais.pop(0)# Aqui iremos escolher qual índice da lista será excluído
print(animais)

#Forma 3 - Usando remove
animais.remove("Ovelha")#Irá remover o item pelo seu conteúdo
print(animais)
