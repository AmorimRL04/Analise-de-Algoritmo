print("16 - [DESAFIO] Escreva um programa em Python para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.")  
print("Ex:")  
print("Digite a quantidade de cigarros fumados por dia: 20")  
print("Digite há quantos anos você fuma: 10")  
print("Você fuma 20 cigarros por dia há 10 anos.")  
print("Isso resultou em uma perda aproximada de 3650 dias de vida.")  

print("1º Passo = Solicitar que o usuário informe a quantidade de cigarros fumados por dia.")  
cigarros_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))  

print("2º Passo = Solicitar que o usuário informe há quantos anos ele fuma.")  
anos_fumando = int(input("Digite há quantos anos você fuma: "))  

print("3º Passo = Definir o tempo perdido por cigarro e a quantidade de minutos em um dia.")  
minutos_perdidos_por_cigarro = 10  
minutos_por_dia = 1440  
dias_por_ano = 365  

print("4º Passo = Calcular a quantidade total de minutos perdidos devido ao hábito de fumar.")  
total_minutos_perdidos = cigarros_dia * minutos_perdidos_por_cigarro * (anos_fumando * dias_por_ano)  

print("5º Passo = Calcular a quantidade de dias de vida perdidos.")  
dias_de_vida = total_minutos_perdidos / minutos_por_dia  

print("6º Passo = Exibir a quantidade de dias de vida que o fumante perdeu.")  
print(f"Você fuma {cigarros_dia} cigarros por dia há {anos_fumando} anos.")  
print(f"Isso resultou em uma perda aproximada de {dias_de_vida:.0f} dias de vida.")  
