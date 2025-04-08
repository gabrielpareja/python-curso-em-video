#Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
#No final, mostre os 10 primeiros termos dessa progressao.
#PA -->Progressão aritmetica ; Sn = (a1 + an).n/2
import time
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
a10 = a1 + (9)*r
for c in range(1,11):
    c1 = a1 + (c - 1)*r
    soma = int((a1 + a10)*r / 2)
    print(f'O {c} termo da PA é: {c1}')
time.sleep(0.5)
print(f'A soma dos 10 primeiros termos é {soma}!')
    
