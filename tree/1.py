import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=rust+malware"

r1 = requests.get(link)
print(r1)