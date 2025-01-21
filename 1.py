import requests
from bs4 import BeautifulSoup
import os
import json

#dictionary = {
#
#}
#
#r1 = requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/1209/periodos/2022/variaveis/1000606?localidades=N1[all]&classificacao=58[92982]")
#
#data = r1.json()
#
#print(json.dumps(data, indent=3))

link = "https://www.bcb.gov.br/estabilidadefinanceira/fechamentodolar"

r1 = requests.get(link)
site = BeautifulSoup(r1.text, "html.parser")
#print(site.prettify())


b2 = site.find("title")
print(b2)

