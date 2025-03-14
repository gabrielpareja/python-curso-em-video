#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
n = str(input('Digite o nome da pessoa para ser analisado: '))
print('O nome {} possui "Silva"? '.format(n))
print("silva" in n.lower()[0:])