atividade = input("Digite o tipo de atividade (caminhada, corrida ou ciclismo): ")
tempo = int(input("Digite o tempo em minutos: "))

if atividade == "caminhada":
  calorias_queimadas = tempo * 5
elif atividade == "corrida":
  calorias_queimadas = tempo * 10
elif atividade == "ciclismo":
  calorias_queimadas = tempo * 8
else:
  print("Atividade inválida.")
  calorias_queimadas = 0

print(f"Você queimou {calorias_queimadas} calorias.")