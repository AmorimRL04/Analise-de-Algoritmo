print("11 - Desenvolva um programa em Python que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta. (fórmula Δ = b² – 4ac)")  
print("Ex:")  
print("Digite o valor de A: 1")  
print("Digite o valor de B: -3")  
print("Digite o valor de C: 2")  
print("O valor de Delta (Δ) é: 1.00")  

print("1º Passo = Solicitar que o usuário informe o valor de A.")  
a = float(input("Digite o valor de A: "))  

print("2º Passo = Solicitar que o usuário informe o valor de B.")  
b = float(input("Digite o valor de B: "))  

print("3º Passo = Solicitar que o usuário informe o valor de C.")  
c = float(input("Digite o valor de C: "))  

print("4º Passo = Calcular o valor de Delta (Δ) usando a fórmula Δ = b² – 4ac.")  
delta = b**2 - 4 * a * c  

print("5º Passo = Exibir o valor de Delta (Δ).")  
print(f"O valor de Delta (Δ) é: {delta:.2f}")  
