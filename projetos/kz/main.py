import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl


steamid64 = '76561198144740064'
url = f'https://kztimerglobal.com/api/v2.0/records/top?steamid64={steamid64}'
resposta = requests.get(url).json()
conteudo = pd.DataFrame.from_dict(resposta)
conteudo.to_excel('arquivo.xlsx')
