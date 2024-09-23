import random

ppt = random.randint(1, 3)
ne = int(input("Escolha um número entre 1 a 3: "))

if ppt == 1 and ne == 3:
    print("Pedra ganha da Tesoura.")
    
if ppt == 1 and ne == 2:
    print("Papel ganha da Pedra.")
    
if ppt == 1 and ne == 3:
    print("Os dois escolheram Pedra.")
    
if ppt == 2 and ne == 3:
    print("Tesoura ganha de Papel.")
    
if ppt == 2 and ne == 2:
    print("Os dois escolheram Papel.")
    
if ppt == 2 and ne == 1:
    print("Os dois escolheram Tesoura.")