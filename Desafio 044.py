#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros
print('Olá boa tarde! Qual o valor do produto que você quer levar? ')
p = float(input('Digite o valor: '))
forma = str(input('Qual a forma de pagamento? '))
if forma == 'à vista':
    print('Como seu pagamento é a vista você tem o desconto de 10%!\nO valor de R${} ficará R${}!'.format(p,(p*0.9)))
elif forma == 'à vista no cartão':
    print('Como seu pagamento é a vista no cartão, você tem o desconto de 5%!\nO valor de R${} ficará R${}!'.format(p,(p*0.95)))
elif forma == '2x no cartão':
    print(f'Como seu pagamento será parcelado em 2x, o preço final será o mesmo de R${p}!')
else:
    print('Como seu pagamento será parcelado em {}, terá o acréscimo de 20% de juros, o preço final será de R${:.2f}!'.format(forma,(p*1.20)))