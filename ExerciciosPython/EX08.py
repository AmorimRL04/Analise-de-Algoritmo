print("8 - Desenvolva um programa em Python que leia uma distância em metros e mostre os valores relativos em outras medidas.")  
print("Ex:")  
print("Digite uma distância em metros: 100")  
print("Distância de 10000 Cm")  

print("1º Passo = Solicitar que o usuário informe uma distância em metros.")  
metros = float(input("Digite uma distância em metros: "))  

print("2º Passo = Calcular a distância em centímetros.")  
centimetros = metros * 100  

print("3º Passo = Exibir o resultado da distância em centímetros.")  
print(f"Distancia de {centimetros:.0f}cm")  
