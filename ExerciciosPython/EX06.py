print("6 - Faça um programa em Python que leia um número inteiro e mostre o seu antecessor e seu sucessor.")  
print("Ex:")  
print("Digite um número: 9")  
print("O antecessor de 9 é 8")  
print("O sucessor de 9 é 10")  

print("1º Passo = Solicitar que o usuário informe um número inteiro.")  
valor = int(input("Digite uma número: "))  

print("2º Passo = Calcular o antecessor do número.")  
antecessor = valor - 1  

print("3º Passo = Calcular o sucessor do número.")  
sucessor = valor + 1  

print("4º Passo = Exibir o antecessor do número.")  
print(f'O antecessor de {valor} é {antecessor}')  

print("5º Passo = Exibir o sucessor do número.")  
print(f'O sucessor de {valor} é {sucessor}')  
