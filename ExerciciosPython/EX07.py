print("7 - Crie um programa em Python que leia um número real e mostre na tela o seu dobro e a sua terça parte.")  
print("Ex:")  
print("Digite um número: 3.5")  
print("O dobro de 3.5 é 7.0")  
print("A terça parte de 3.5 é 1.166666")  

print("1º Passo = Solicitar que o usuário informe um número real.")  
valor = float(input("Digite uma número: "))  

print("2º Passo = Calcular o dobro do número.")  
dobro = valor * 2  

print("3º Passo = Calcular a terça parte do número.")  
terça = valor / 3  

print("4º Passo = Exibir o resultado do dobro.")  
print(f'O dobro de {valor} é {dobro}')  

print("5º Passo = Exibir o resultado da terça parte, com precisão de 6 casas decimais.")  
print(f'A terça parte de {valor} é {terça:.6f} ')  
