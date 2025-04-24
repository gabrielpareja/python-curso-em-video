#crie um programa que leia o ano de nascimento de 7 pessoas.
#No final mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1,8):
    ano = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    idade = atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade!')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade!')


