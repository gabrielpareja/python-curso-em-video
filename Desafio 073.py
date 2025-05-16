#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
times = ('Palmeiras' , 'Red Bull Bragantino' , 'FLAMENGO' , 'CRUZEIRO' , 'FLUMINENCE' , 'BAHIA' , 'CEARÁ' , 'CORINTHIANS' , 'INTERNACIONAL' , 'ATLÉTICO-MG' , 'SÃO PAULO' , 'BOTAFOGO' , 'GRÊMIO' , 'VASCO' , 'JUVENTUDE' , 'MIRASSOL' , 'FORTALEZA' , 'VITÓRIA' , 'SANTOS' , 'SPORT')
print(f'Os primeiros 5 times são : {times[0:5]}')
print('~~' * 30)
print(f'Os últimos 4 colocados são : {times[-4:]}')
print('~~' * 30)
print(f'Os times em ordem alfabética fica {sorted(times)}')
print('~~' * 30)
print(f'O time Vasco está na {times.index("VASCO")+1} posição.')
print('~~' * 30)