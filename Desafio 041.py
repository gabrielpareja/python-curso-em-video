# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER
a = int(input('Qual a data de nascimento do atleta? '))
i = 2025 - a
if i <= 9:
    print('O atleta com {} anos é um atleta Mirim.'.format(i))
elif 9 < i <= 14:
    print('O atleta com {} anos é infantil.'.format(i))
elif 14 < i <= 19:
    print('O atleta com {} anos é junior.'.format(i))
elif i == 20:
    print('O atleta com {} anos é sênior.'.format(i))
elif i > 20:
    print('O atleta de {} anos é um atleta master.'.format(i))