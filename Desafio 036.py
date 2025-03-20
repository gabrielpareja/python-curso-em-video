#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
print('Então você deseja comprar a casa através de um empréstimo bancário, vamos analisar seu caso. ')
c = float(input('Qual o valor da casa que deseja comprar: R$ '))
s = float(input('Qual o seu salário atual: R$ '))
a = int(input('Em quantos anos deseja pagar a casa: '))
if c/(a*12) > s*0.3:
    print('O empréstimo foi negado, pois a parcela mensal excede 30% do seu salário!')
else:
    print('O empréstimo foi aprovado! A parcela mensal será de R${:.2f}'.format(c/(a*12)))
