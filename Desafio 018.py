#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,cosseno e a tangente desse angulo
import math
a = float(input('Cite um ângulo: '))
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print(f'O seno é {s}. \nO cosseno é {c}. \nA tangente é {t}.')