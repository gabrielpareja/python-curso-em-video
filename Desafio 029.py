#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.
print('ZUUUUUMMMMM.....')
v = int(input('Qual a velocidade que apareceu no radar? '))
m = (v - 80) * 7
if v<= 80:
    print('Está dentro do limite de velocidade, tudo ok!')
else:
    print('VELOCIDADE ACIMA DO LIMITE!!!')
    print('A multa será de RS{:.2f} !'.format(m))
