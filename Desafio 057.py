#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo inválido, digite entre [M/F]: ')).strip().upper()[0]
print(f'Seu sexo foi registrado como {sexo}!')