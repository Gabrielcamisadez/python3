import pandas as pd
import requests
import os
from flask import Flask, jsonify




#               INITIALIZATION
#========================================================

app = Flask(__name__)


#                   FUNCTIONALITY
#========================================================

@app.route('/pegarjson')
def pegarjson():
    tabela = pd.read_csv('password_wordlist.txt')
    return jsonify(tabela.to_dict())


@app.route('/pegaruser')
def pegaruser():
    tabela = pd.read_csv('username_wordlist.txt')
    return jsonify(tabela.to_dict())
    

#                   Running
#========================================================
app.run()

    
