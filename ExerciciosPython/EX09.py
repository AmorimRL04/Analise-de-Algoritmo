print("9 - Faça um programa em Python que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.")  
print("Ex:")  
print("Quanto dinheiro tem na carteira: 100")  
print("Você pode comprar com R$100 um total de U$28,99")  

print("1º Passo = Definir a cotação do dólar.")  
dolar = 3.45  

print("2º Passo = Solicitar que o usuário informe quanto dinheiro tem na carteira.")  
carteira = float(input("Quanto dinheiro tem na carteira: "))  

print("3º Passo = Calcular quantos dólares a pessoa pode comprar com o valor informado.")  
calculo = carteira / dolar  

print("4º Passo = Exibir o resultado, informando o valor em dólares.")  
print(f"Você pode comprar com R${carteira} um total de U${calculo:.2f}")  
