print("15 - Crie um programa Python que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.")  
print("Ex:")  
print("Dias trabalhados em um mês: 20")  
print("O funcionário trabalhou 20 dias, 8 horas por dia, com um ganho de R$ 25 por hora, totalizando um salário de R$ 4000.00 neste mês.")  

print("1º Passo = Solicitar que o usuário informe o número de dias trabalhados no mês.")  
dias_trabalhados = int(input("Dias trabalhados em um mês: "))  

print("2º Passo = Definir o número de horas trabalhadas por dia e o valor ganho por hora.")  
horas_trabalhadas = 8  
ganho_hora_trabalhada = 25  

print("3º Passo = Calcular o salário do funcionário com base nas horas trabalhadas e no ganho por hora.")  
salario_funcionario = (horas_trabalhadas * ganho_hora_trabalhada) * dias_trabalhados  

print("4º Passo = Exibir as informações do salário do funcionário.")  
print(f"O funcionário trabalhou {dias_trabalhados} dias, {horas_trabalhadas} horas por dia, ")  
print(f"com um ganho de R$ {ganho_hora_trabalhada} por hora, totalizando um salário de R$ {salario_funcionario:.2f} neste mês.")  
