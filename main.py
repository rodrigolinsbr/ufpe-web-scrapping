import webscraping
import requests


url = 'https://www.meucarronovo.com.br/carro/detalhe/chevrolet-spin-lt-18-8v-econoflex-5p-mec-2015-prata-flex-42802-mcn-8521893'
r = requests.get(url)
print(r.content)