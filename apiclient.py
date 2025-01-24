import requests
import os
from flask import jsonify
import sys

link = "http://127.0.0.1:5000/pegaruser"

r1 = requests.get(link)
print(f'{r1.json()}')






