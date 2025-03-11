print("12 - Crie um programa em Python que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.")  
print("Ex:")  
print("Digite o valor do produto: R$100")  
print("O PREÇO PROMOCIONAL, com 5% de desconto é de R$95.00")  

print("1º Passo = Solicitar que o usuário informe o valor do produto.")  
valor_produto = float(input("Digite o valor do produto: R$"))  

print("2º Passo = Calcular o preço promocional aplicando 5% de desconto.")  
desconto = valor_produto - (valor_produto * 0.05)  

print("3º Passo = Exibir o valor do preço promocional com o desconto.")  
print(f"O PREÇO PROMOCIONAL, com 5% de desconto é de R${desconto:.2f}")  
