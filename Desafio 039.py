#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
n = int(input('Digite o ano de nascimento da pessoa: '))
i = 2025 - n
l = i - 18
a = 2025 - l
f = 2025 + (18-i)
print('Quem nasceu em {} tem {} anos em 2025'.format(n,i))
if i < 18:
    print('Você tem menos de 18 anos!\nVocê deverá se alistar somente em {}!'.format(f))
elif i == 18:
    print('Você tem 18 anos! Você deve se alistar ainda este ano, fique atento!')
elif i > 18:
    print('Você tem mais de 18 anos!\nVocê devia ter se alistado no ano de {}!'.format(a))
