#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#OBS: Um ano Bisexto é necessariamente divisível por 4
a = int(input('Digite um ano para saber se ele é ou não Bissexto: '))
if a % 4 == 1:
    print('O ano de {} é Bissexto!'.format(a))
else:
    print('O ano de {} não é Bissexto!'.format(a))