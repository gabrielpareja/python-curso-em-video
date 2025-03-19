#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200 Km.
#Para viagens mais longas que 200 km será cobrado R$0,45
d = int(input('Qual a distância que você deseja realizar a viagem? '))
d1 = d * 0.45
d2 = d * 0.50
if d > 200:
    print('Como a viagem acima de 200 km é mais barata, o valor será R${:.2f}'.format(d1))
else:
    print('O valor da viagem de {} quilômetros será R${:.2f}. '.format(d,d2))