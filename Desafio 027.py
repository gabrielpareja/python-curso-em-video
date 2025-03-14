#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Qual o nome da pessoa para ser analisado? '))
nome = n.split()
primeiro = nome[0]
último = nome[-1]
print('O primeiro nome é {}!'.format(primeiro))
print('O último nome é {}!'.format(último))