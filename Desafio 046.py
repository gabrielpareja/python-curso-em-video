#Faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio
#Indo de 10 ate 0, com pausa de 1 segundo entre eles.
import time
print('==========Contagem para estouro de fogos de artificio==========')
for c in range(10 , -1 , -1):
    print(c)
    time.sleep(1)
print('KABUUUUMMMM')