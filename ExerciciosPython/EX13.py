print("13 - Faça um programa em Python que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.")  
print("Ex:")  
print("Digite o valor do salário: R$1500")  
print("O seu novo salário, com 15% de aumento é de R$1725.00")  

print("1º Passo = Solicitar que o usuário informe o salário do funcionário.")  
salario_funcionario = float(input("Digite o valor do salário: R$"))  

print("2º Passo = Calcular o novo salário com 15% de aumento.")  
aumento = salario_funcionario + (salario_funcionario * 0.15)  

print("3º Passo = Exibir o novo salário com o aumento de 15%.")  
print(f"O seu novo salário, com 15% de aumento é de R${aumento:.2f}")  
