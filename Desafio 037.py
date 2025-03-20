#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
# os códigos que transformam o número em binário, octal e hexadecimal são respectivamente: bin() ; oct() ; hex(10)
n = int(input('Diga um número para ser transformado: '))
o = int(input('Escolha a base de conversão: \n 1 --> Binário \n 2 --> Octal \n 3 --> Hexadecimal \n --> '))
if o == 1:
    print('O número convertido em binário será : {}!'.format(bin(n)))
elif n == 2:
    print('O número convertido em octal será : {}!'.format(oct()))
elif o == 3:
    print('O número convertido em hexadecimal será : {}!'.format(hex(n)))

