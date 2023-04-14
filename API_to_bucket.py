import requests
import boto3 
import json

# Chave de API da Alpha Vantage
api_key = '2ULLERBG34DUQAKS'

# URL da API Alpha Vantage para solicitar os dados do IBM com intervalo de 5min
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={api_key}'

# Faz a chamada à API e armazena a resposta em uma variável
response = requests.get(url)

# Converte a resposta em formato JSON
data = response.json()

# Verifica se a chave "Time Series (5min)" está presente no dicionário JSON
if 'Time Series (5min)' in data:
    # Cria um arquivo CSV e escreve os dados nele
    with open('ibm_5min.json', mode='w', newline='') as file:
        json.dump(data, file)
else:
    print('Dados não encontrados')


# Configura as credenciais do AWS
s3 = boto3.resource('s3', aws_access_key_id='beathrizdev@gmail.com', aws_secret_access_key='Pedro2Pedro@')

# Nome do bucket que você deseja usar
bucket_name = 'datafinance'

# Nome do arquivo JSON que você deseja salvar no bucket
json_file_name = 'ibm_5min.json'


# Salva o arquivo JSON no bucket
s3.Object(bucket_name, json_file_name).put(Body=(bytes(json.dumps(data).encode('UTF-8'))))
