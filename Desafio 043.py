#O Índice de Massa Corporal (IMC) é calculado dividindo o peso em quilos pela altura em metros ao quadrado. A fórmula é IMC = peso / (altura x altura). 
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
print('==========Calculadora de IMC==========')
p = float(input('Digite seu peso em KG: '))
a = float(input('Digite sua altura em metros: '))
imc = p / (a**2)
if imc < 18.5:
    print('Seu índice de massa corporal é {:.2f}! Você está abaixo do peso.'.format(imc))
elif 18.5 < imc < 25:
    print('Seu índice de massa corporal é {:.2f}! Você está no peso ideal!'.format(imc))
elif 25 < imc < 30:
    print('Seu índice de massa corporal é {:.2f}! Você está em sobrepeso!'.format(imc))
elif 30 < imc < 40:
    print('Seu índice de massa corporal é {:.2f}! Você está obeso!'.format(imc))
elif 40 < imc:
    print('Seu índice de massa corporal é {:.2f}! Você está com obesidade mórbida, procure um médico!')