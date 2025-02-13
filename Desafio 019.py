#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele , lendo o nome deles e escrevendo o nome do escolhido.
import random
nome = str(input('Cite nome 1: '))
nome2 = str(input('Cite nome 2: '))
nome3 = str(input('Cite nome 3: '))
nome4 = str(input('Cite nome 4: '))
nomes = [nome , nome2 , nome3 , nome4]
print(f'O professor escolheu {random.choice(nomes)}!')