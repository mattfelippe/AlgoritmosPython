#Matheus Moreira TP5 - Projeto de Bloco - Arquitetura de Computadores, Sistemas Operacionais e Redes

import time
import json
import requests

#Pegar url
url = 'http://api.openweathermap.org/data/2.5/weather?id=3451190&appid=39208ec8ec8b901c9d26d11746d5269a&units=metric&lang=pt'

pegarDadosPagina = requests.post(url, json={'key': 'value'})
content = pegarDadosPagina.json()

#Declarar variáveis e pegar valor
cidade = (content['name'])
temp_min = (content['main']['temp_min'])
temp_max = (content['main']['temp_max'])
direcao_do_vento = (content['wind']['deg'])
nascer_do_sol = (content['sys']['sunrise'])
por_do_sol = (content['sys']['sunset'])

#Lógica cálculo direção do vento
def direcao_vento():
    if direcao_do_vento == 0:
        return('Norte')
    if (direcao_do_vento > 0) and (direcao_do_vento < 90):
        return('Nordeste')
    if direcao_do_vento == 90:
        return('Leste')
    if (direcao_do_vento > 90) and (direcao_do_vento < 180):
        return('Sudeste')
    if direcao_do_vento == 180:
        return('Sul')
    if (direcao_do_vento > 180) and (direcao_do_vento < 270):
        return('Sudoeste')
    if direcao_do_vento == 270:
        return('Oeste')
    if (direcao_do_vento > 270) and (direcao_do_vento < 360):
        return('Noroeste')

#Organização das variáveis
direcao = (direcao_vento())
nascente = (time.strftime("%D %H:%M", time.localtime(int(nascer_do_sol))))
poente = (time.strftime("%D %H:%M", time.localtime(int(por_do_sol))))

#Relatório
print('')
print('---------- Relátório ----------')
print(cidade)
print(f'Temperatura Mínima:',(temp_min),'ºC')
print(f'Temperatura Máxima:',(temp_max),'ºC')
print(f'Direção do Vento:',(direcao_vento()))
print(f'Nascer do Sol:', (nascente))
print(f'Por do Sol:',(poente))
print('')
print('Informações geradas na tela inserida e carregada em dados_clima.json')

#Junção de dados em um dicionário
dados_clima = {"Cidade": cidade, 'Temperatura minima': temp_min, 'Temperatura maxima': temp_max, 'Direcao do vento': direcao, 'Nascer do Sol': nascente, 'Por do Sol': poente}

#Função para gerar o arquivo dados_clima.json
def gerar_json(content, dados_clima):
    with open('dados_clima.json', 'w') as f:
        json.dump(dados_clima, f)
    print('')
    print('**Arquivo gerado na pasta onde esse arquivo se encontra. Arquivo dados_clima.json**')

#Exibir os dados do dicionário com o espaçamento 4
print(json.dumps(dados_clima, indent = 4))

#Chamada do método para gerar o arquivo JSON
gerar_json(content, dados_clima)