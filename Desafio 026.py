#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
#Quantas vezes aparece a letra "A"  
#Em que posição aparece a primeira vez  
#Em que posição aparece pela ultima vez
n = str(input('Digite um nome para ser analisado : ')).upper()
print('O Nome {} possui {} letras "A". '.format(n,n.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}!'.format(n.find('A')+1))
print('A letra "A" aparece pela ultima vez na posição {}!'.format(n.rfind("A")+1))
