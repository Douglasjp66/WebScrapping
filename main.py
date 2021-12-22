import csv

from bs4 import BeautifulSoup
import requests
from config import URL_BASE,URL

paginas = []

#CRIANDO UM CSV FILE
arquivo_csv = csv.writer(open('Nome_Artistas_Z.csv','w',newline='\n'))
arquivo_csv.writerow(['Nomes_Artistas','URL_Artistas'])




for num_page in range(1, 5):
    paginas.append(f"https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ{num_page}.htm")

for url_por_pagina in paginas:
    pagina = requests.get(url_por_pagina)
    soup = BeautifulSoup(pagina.text, 'html.parser')# Parser >> analizador de html
    # REMOVER LINKS ANTERIORES
    ultimos_links = soup.find(class_='AlphaNav')
    ultimos_links.decompose()

    # Pegar conteúdo da body class
    bloco_nomes_artistas = soup.find(class_='BodyText')

    # Printa a lista de artistas da PAGINA  com link, referência ao <a href> em linha
    lista_nomes_artistas = bloco_nomes_artistas.find_all('a') # Printa a lista de artistas da PAGINA  com link, referência ao  <a href> tudo em uma linha

    # PRINTANDO OS NOMES E LINKS DA LISTA DE ARTISTAS ORGANIZADOS, PROXIMO PASSO SALVAR EM ARQUIVO CSV
    for nome_artista in lista_nomes_artistas:
        nomes = nome_artista.contents[0]
        links = f"{URL_BASE}{nome_artista.get('href')}"
        arquivo_csv.writerow([nomes, links])
        print(nomes)
        print(links)




