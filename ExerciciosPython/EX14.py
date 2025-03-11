print("14 - A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa em Python que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$ 90,00 por dia e R$ 0,20 por Km rodado.")  
print("Ex:")  
print("Digite quantos Km o carro alugado percorreu: 100")  
print("Digite por quantos dias o carro foi alugado: 5")  
print("O carro foi alugado por 5 dias e percorreu 100.00 Km.")  
print("O preço total a pagar é de R$ 950.00")  

print("1º Passo = Solicitar que o usuário informe a quantidade de Km percorridos pelo carro.")  
km_percorridos = float(input("Digite quantos Km o carro alugado percorreu: "))  

print("2º Passo = Solicitar que o usuário informe a quantidade de dias que o carro foi alugado.")  
dias_alugado = int(input("Digite por quantos dias o carro foi alugado: "))  

print("3º Passo = Definir o preço por Km percorrido e o preço diário de aluguel.")  
preco_km = 0.20  
preco_diaria = 90.00  

print("4º Passo = Calcular o preço total a pagar com base nos Km percorridos e dias alugados.")  
total_a_pagar = (preco_km * km_percorridos) + (preco_diaria * dias_alugado)  

print("5º Passo = Exibir o total a pagar e as informações de aluguel.")  
print(f"O carro foi alugado por {dias_alugado} dias e percorreu {km_percorridos:.2f} Km.")  
print(f"O preço total a pagar é de R$ {total_a_pagar:.2f}")  
