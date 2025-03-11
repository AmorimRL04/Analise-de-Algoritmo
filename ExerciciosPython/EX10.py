print("10 - Faça um programa em Python que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.")  
print("Ex:")  
print("Digite a largura: 5")  
print("Digite a altura: 4")  
print("A área que será pintada será de 20.00m², sendo necessário 10.00 litro de tinta.")  

print("1º Passo = Solicitar que o usuário informe a largura da parede.")  
largura = float(input("Digite a largura: "))  

print("2º Passo = Solicitar que o usuário informe a altura da parede.")  
altura = float(input("Digite a altura: "))  

print("3º Passo = Calcular a área da parede.")  
area = largura * altura  

print("4º Passo = Calcular a quantidade de tinta necessária para pintar a área.")  
litros_necessários = area / 2  

print("5º Passo = Exibir a área a ser pintada e a quantidade de tinta necessária.")  
print(f"A área que será pintada será de {area:.2f}m², sendo necessário {litros_necessários} litro de tinta.")  
