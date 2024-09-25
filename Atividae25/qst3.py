def converter_temperatura(celsius, unidade): 
    #Converte a temperatura em Celsius para Fahrenheit ou Kelvin.
    if unidade == "Fahrenheit":
        resultado = (9/5) * celsius + 32
        print(f"{celsius}°C equivalem a {resultado:.2f}°F")
    elif unidade == "Kelvin":
        resultado = celsius + 273.15
        print(f"{celsius}°C equivalem a {resultado:.2f} K")
    else:
        print("Unidade inválida")

while True:
    # Solicita ao usuário a temperatura em Celsius
    celsius = float(input("Digite a temperatura em graus Celsius (ou um valor negativo para sair): "))
    
    if celsius < 0:
        print("Programa encerrado.")
        break
    
    # Solicita ao usuário a unidade desejada para conversão
    unidade = input("Para qual unidade deseja converter? (Fahrenheit ou Kelvin): ")
    
    # Realiza a conversão
    converter_temperatura(celsius, unidade)