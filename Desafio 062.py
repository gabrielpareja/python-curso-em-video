#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))

termo = a1
contador = 0
mais = 10  # mostra os primeiros 10 termos

while mais != 0:
    total = contador + mais  # novo total de termos a exibir
    while contador < total:
        print(f'{termo}', end=' ➔ ' if contador < total - 1 else '')
        termo += r
        contador += 1
    print('\nPAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'\nProgressão finalizada com {contador} termos!')
