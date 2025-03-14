#Faça um programa que leia o nome completo de uma pessoa e mostre:
#>Nome com todas letras maiúsculas.
#>Nome com todas letras minusculas.
#>Quantas letras ao todo.
#>Quantas letras tem o primeiro nome.
n = str(input('Digite o nome da pessoa para ser analisado : ')).strip()
print('O nome em letras maiúsculas é {}'.format(n.upper()))
print('O nome em letras minúsculas é {}'.format(n.lower()))
print('A quantitade de letras é : {}'.format(len(n)-n.count(' ')))
print('O primeiro nome possui {} letras'.format(n.find(' ')))

