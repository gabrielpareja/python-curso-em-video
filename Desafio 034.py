#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00 , calcule um aumento de 10%.
#Para os inferiores ou iguais , o aumento é de 15%.
s = float(input('Qual o salário que iremos analisar: '))
if s > 1250:
    print('O aumento do salário será de 10%! Dando o total de R${:.2f}'.format(s*1.1))
else:
    print('O aumento do salário será de 15%! Dando o total de R${:.2f}'.format(s*1.15))