print("3 - Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.")  
print("Ex:")  
print("Nome do Funcionário: Maria do Carmo")  
print("Salário: 1850,45")  
print("O funcionário Maria do Carmo tem um salário de R$1850,45 em junho.")  

print("1º Passo = Solicitar que o usuário informe o nome do funcionário.")  
nome = str(input("Nome do Funcionário: "))  

print("2º Passo = Solicitar que o usuário informe o salário do funcionário.")  
salario = float(input("Salário: "))  

print("3º Passo = Exibir a mensagem final com os dados do funcionário.")  
print(f"O funcionário {nome} tem um salário de R${salario} em junho.")  
