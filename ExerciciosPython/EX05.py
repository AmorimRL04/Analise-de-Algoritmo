print("5 - Faça um programa em Python que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.")  
print("Ex:")  
print("Nota 1: 4.5")  
print("Nota 2: 8.5")  
print("A média entre 4.5 e 8.5 é igual a 6.5")  

print("1º Passo = Solicitar que o usuário informe a primeira nota.")  
valor1 = float(input("Nota 1: "))  

print("2º Passo = Solicitar que o usuário informe a segunda nota.")  
valor2 = float(input("Nota 2: "))  

print("3º Passo = Calcular a média entre as duas notas.")  
media = (valor1 + valor2) / 2  

print("4º Passo = Exibir o resultado da média.")  
print(f"A média entre {valor1} e {valor2} é igual a {media}.")  
