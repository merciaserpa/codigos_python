import random

# O computador escolhe um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas_restantes = 5

print("Bem-vindo ao jogo da adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100. Você tem 5 tentativas.")

while tentativas_restantes > 0:
    palpite = int(input("Digite seu palpite: "))
    
    if palpite < numero_secreto:
        print("O número secreto é maior.")
    elif palpite > numero_secreto:
        print("O número secreto é menor.")
    else:
        print("Parabéns! Você adivinhou o número secreto!")
        break
    
    tentativas_restantes -= 1
    print(f"Tentativas restantes: {tentativas_restantes}")

if tentativas_restantes == 0:
    print(f"Você não conseguiu adivinhar. O número secreto era {numero_secreto}.")